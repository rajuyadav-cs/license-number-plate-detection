import cv2
import easyocr

_reader = None


def get_reader():
    global _reader

    if _reader is None:
        _reader = easyocr.Reader(["en"], gpu=False)

    return _reader


def read_plate_text(image_path):
    try:
        image = cv2.imread(str(image_path))

        if image is None:
            return None

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        reader = get_reader()
        results = reader.readtext(image_rgb)

        if not results:
            return None

        best_result = max(results, key=lambda item: item[2])
        text = best_result[1]

        return text.replace(" ", "").upper()

    except Exception as error:
        print("OCR Error:", error)
        return None