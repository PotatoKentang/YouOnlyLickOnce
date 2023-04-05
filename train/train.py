from ultralytics import YOLO
import os
import numpy as np
from PIL import Image
import base64

model = YOLO("./yolov8x.pt")  # build from YAML and transfer weights

def check_available_gpu():
    import torch
    print("checking cuda")
    print(torch.cuda.is_available())
    print(torch.cuda.device_count())
    print(torch.cuda.get_device_name(0))
    print(torch.cuda.current_device())
    print("finished checking cuda")


def predict(imgFile):
    # Inference
    img = Image.open(imgFile)  # PIL image
    img = np.array(img)  # numpy array
    results = model(img,conf=0.8,boxes=True)  # list of Results objects
    for result in results:
        predicted_class = [model.names[int(classIndex)] for classIndex in result.boxes.cls]
        # print(predicted_class)
        #don't touch this
        res_plotted = result.plot()
        PIL_image = Image.fromarray(res_plotted)
        encoded_image = base64.b64encode(PIL_image.tobytes()).decode("utf-8")
    #delete logic
    return predicted_class, encoded_image

def train_start():
    #error kemungkinan karena ngeloadnya ke directory lain dimana python gk ngerti .. kebelakang
    # Load a model
    predict(model)

    # Train the model
    # dirname = os.path.dirname(__file__,)
    # filename = os.path.join(dirname, "data.yaml").replace("\\","/")
    # model.train(data="coco128.yaml", epochs=100, imgsz=640,verbose=True,device=0,cache=True)
    # results = model.val()
    # print(results)
    # success = model.export(format="onnx")
    # print(success)

if __name__ == '__main__':
    check_available_gpu()
    train_start()
    