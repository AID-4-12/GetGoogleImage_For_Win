from ultralytics import YOLO
# import torch

model = YOLO('yolov8s-cls.yaml')
model = YOLO('yolov8s-cls.pt')

model.train(data='C:/Users/imnyang/Nextcloud/train_dataset/', epochs=20)