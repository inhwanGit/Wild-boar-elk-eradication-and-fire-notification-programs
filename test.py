from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

model = YOLO("best.pt")
results = model.predict(source=0, show = True)
