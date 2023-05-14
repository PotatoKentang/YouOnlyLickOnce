# YouOnlyLickOnce Backend for Peneliti Kentang

Welcome to YouOnlyLickOnce backend repository built with flask and YOLOv8 model

For the frontend, please refer to the [PenelitiKentang](https://github.com/PotatoKentang/SangPenelitiKentang) repository

## 📊 Requirements

- Python
- Pipenv

## 🛠 Setup

Clone the repository

```bash
git clone https://github.com/PotatoKentang/YouOnlyLickOnce
```

Install the dependencies

```bash
python -m pipenv shell
pip install -r requirements.txt
```

To start the application, run

```bash
python -m pipenv shell
python app.py
```

## 📍 End Point

> 1. /: GET endpoint that returns a welcome message.
> 2. /list_of_ingredients: POST endpoint that receives a search query as input and returns a list of ingredients that match the query.
> 3. /list_of_ingredients/<id>: POST endpoint that receives an ingredient ID as input and returns information about the corresponding ingredient.
> 4. /get_nutrients: POST endpoint that receives a food query as input and returns the nutritional information of the corresponding food.
> 5. /predict_food: POST endpoint that receives an image file as input and returns the predicted label and image.

## 📱 Usage

> 1. To fetch query of food from front-end
> 2. Detect food images from post requests

Built With the help of:

> 1. Dataset preprocessing: Roboflow ->https://universe.roboflow.com/search?q=food or https://universe.roboflow.com/abraham-kristanto/final-food-dataset
> 2. Hoped Dataset: https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/
> 3. Comet: Training Visualizer
> 4. calorieninjas: https://calorieninjas.com/api

