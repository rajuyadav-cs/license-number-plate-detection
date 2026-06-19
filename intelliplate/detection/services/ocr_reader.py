import cv2
import easyocr

reader = easyocr.Reader(["en"], gpu=False)


def read_plate_text(image_path):
    try:
        image = cv2.imread(str(image_path))

        if image is None:
            return None

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = reader.readtext(image_rgb)

        if not results:
            return None

        best_result = max(results, key=lambda item: item[2])
        text = best_result[1]

        return text.replace(" ", "").upper()

    except Exception as error:
        print("OCR Error:", error)
        return None