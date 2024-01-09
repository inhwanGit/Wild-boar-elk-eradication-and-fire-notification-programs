from ultralytics import YOLO
import torch

def run():
    torch.multiprocessing.freeze_support()
    # Load a model
    model = YOLO("yolov8n.pt")  # build a new model from scratch
    # Use the model
    model.train(data="animal.yaml", epochs=300)  # train the model


if __name__ == '__main__':
    run()


