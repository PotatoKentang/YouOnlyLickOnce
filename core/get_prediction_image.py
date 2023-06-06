from ultralytics import YOLO
from flask import send_file
import os
import numpy as np
from PIL import Image
import io

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,"../model/yoloTrained.pt")
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

food_map = {
    'ayam': 'chicken',
    'blueberry-muffin': 'blueberry muffin',
    'bubur': 'porridge',
    'burger': 'burger',
    'chocolate-chip-cookie': 'chocolate chip cookie',
    'croissant': 'croissant',
    'doughnut': 'doughnut',
    'es-pisang-ijo': 'green banana ice',
    'french-fries': 'French fries',
    'ikan-goreng': 'fried fish',
    'kacang-mete': 'cashew nuts',
    'kangkung': 'water spinach',
    'klepon': 'klepon',
    'kopi-hitam': 'black coffee',
    'macaroni-cheese': 'macaroni and cheese',
    'martabak-manis': 'sweet martabak',
    'mie-ayam': 'chicken noodle',
    'nasi-goreng': 'fried rice',
    'nasi-putih': 'white rice',
    'onde-onde': 'onde-onde',
    'pancake': 'pancake',
    'pempek': 'pempek',
    'pizza': 'pizza',
    'red-velvet': 'red velvet',
    'rendang': 'rendang',
    'roti-slice': 'bread slice',
    'salad': 'salad',
    'salmon': 'salmon',
    'sate': 'satay',
    'sayur-asem': 'tamarind soup',
    'seafood': 'seafood',
    'semangka': 'watermelon',
    'soto-ayam': 'chicken soup',
    'spaghetti-bolognese': 'spaghetti bolognese',
    'steak': 'steak',
    'sushi-makizushi': 'sushi roll',
    'sushi-nigiri': 'nigiri sushi',
    'telur-balado': 'spicy fried egg',
    'telur-dadar': 'omelette',
    'telur-mata-sapi': 'sunny-side-up egg'
}

def predict_image(imgFile):
    # Inference
    img = Image.open(imgFile)  # PIL image
    img = np.array(img)  # numpy array
    results = model(img,conf=0.15,boxes=True)  # list of Results objects
    for result in results:
        predicted_class = [food_map.get(model.names[int(classIndex)]) for classIndex in result.boxes.cls]
        # print(predicted_class)
        #don't touch this
        res_plotted = result.plot()
        PIL_image = Image.fromarray(res_plotted)
        imageLink = "image link"
    #delete logic
        return predicted_class,imageLink


if __name__ == '__main__':
    check_available_gpu()


