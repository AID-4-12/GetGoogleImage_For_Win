from ultralytics import YOLO
# import torch

model = YOLO('yolov8s-cls.yaml')
model = YOLO('yolov8s-cls.pt')

model.train(data='C:/Users/imnyang/Desktop/GetGoogleImage/train_dataset/cat', epochs=20)