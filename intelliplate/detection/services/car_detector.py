import cv2
import numpy as np
import tensorflow as tf
from ultralytics import YOLO

image_path = "media/uploads/test.jpg"

plate_model_path = "ml_models/licence_plate_detection.pt"
text_model_path = "ml_models/license_plate_model_final.h5"

plate_model = YOLO(plate_model_path)
text_model = tf.keras.models.load_model(text_model_path)

image = cv2.imread(image_path)

results = plate_model(image)
result = results[0]

for box in result.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    plate_crop = image[y1:y2, x1:x2]

    resized = cv2.resize(plate_crop, (256, 64))
    resized = resized.astype("float32") / 255.0
    resized = np.expand_dims(resized, axis=0)

    prediction = text_model.predict(resized)

    print("Prediction shape:", prediction.shape)
    print("Argmax:", np.argmax(prediction, axis=-1))