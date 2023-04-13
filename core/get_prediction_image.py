from ultralytics import YOLO
from flask import send_file
import os
import numpy as np
from PIL import Image
import io

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,"../model/yoloTrained1.pt")
fullPathNorm = os.path.normpath(filename)
model = YOLO(fullPathNorm)
# model = YOLO("yolov8x.pt") #load if you don't have a model locally


def check_available_gpu():
    import torch
    print("checking cuda")
    print(torch.cuda.is_available())
    print(torch.cuda.device_count())
    print(torch.cuda.get_device_name(0))
    print(torch.cuda.current_device())
    print("finished checking cuda")


def predict_image(imgFile):
    # Inference
    img = Image.open(imgFile)  # PIL image
    img = np.array(img)  # numpy array
    results = model(img,boxes=True)  # list of Results objects
    for result in results:
        predicted_class = [model.names[int(classIndex)] for classIndex in result.boxes.cls]
        # print(predicted_class)
        #don't touch this
        res_plotted = result.plot()
        PIL_image = Image.fromarray(res_plotted)
        imageLink = "image link"
    #delete logic
    return predicted_class,imageLink


if __name__ == '__main__':
    check_available_gpu()


