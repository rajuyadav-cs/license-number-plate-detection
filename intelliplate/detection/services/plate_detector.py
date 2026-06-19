from pathlib import Path
import urllib.request
import cv2
from django.conf import settings


MODEL_URL = "https://huggingface.co/rajuyadav-cs/licence-number-plate-detection/resolve/main/licence_plate_detection.pt"
MODEL_DIR = settings.BASE_DIR / "ml_models"
MODEL_PATH = MODEL_DIR / "licence_plate_detection.pt"

_model = None


def download_model_if_missing():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    if not MODEL_PATH.exists():
        print("Downloading YOLO model from Hugging Face...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("YOLO model downloaded successfully.")


def get_model():
    global _model

    if _model is None:
        from ultralytics import YOLO

        download_model_if_missing()
        _model = YOLO(str(MODEL_PATH))

    return _model


def detect_license_plate(image_path):
    image_path = Path(image_path)
    image = cv2.imread(str(image_path))

    if image is None:
        return {
            "plate_number": None,
            "result_image_url": None,
            "result_image_path": None,
            "plate_crop_url": None,
            "plate_crop_path": None,
            "detections_count": 0,
            "confidence": 0.0,
        }

    model = get_model()

    results = model(image)
    result = results[0]

    plate_crop_url = None
    plate_crop_relative_path = None
    best_confidence = 0.0
    plate_number = None

    for index, box in enumerate(result.boxes):
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = float(box.conf[0])

        if confidence > best_confidence:
            best_confidence = confidence

            plate_crop = image[y1:y2, x1:x2]

            crop_filename = f"plate_crop_{image_path.stem}_{index}.jpg"
            crop_relative_path = Path("plate_crops") / crop_filename
            crop_path = settings.MEDIA_ROOT / crop_relative_path

            crop_path.parent.mkdir(parents=True, exist_ok=True)
            cv2.imwrite(str(crop_path), plate_crop)

            plate_crop_relative_path = str(crop_relative_path).replace("\\", "/")
            plate_crop_url = f"{settings.MEDIA_URL}{plate_crop_relative_path}"

        label_text = f"Plate {confidence:.2f}"

        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(
            image,
            label_text,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2,
        )

    result_filename = f"result_{image_path.name}"
    result_relative_path = Path("results") / result_filename
    result_path = settings.MEDIA_ROOT / result_relative_path

    result_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(result_path), image)

    result_relative_path_str = str(result_relative_path).replace("\\", "/")

    return {
        "plate_number": plate_number,
        "result_image_url": f"{settings.MEDIA_URL}{result_relative_path_str}",
        "result_image_path": result_relative_path_str,
        "plate_crop_url": plate_crop_url,
        "plate_crop_path": plate_crop_relative_path,
        "detections_count": len(result.boxes),
        "confidence": round(best_confidence, 2),
    }