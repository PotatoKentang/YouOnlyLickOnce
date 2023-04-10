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

## 📱 Usage

1. To fetch query of food from front-end
2. Detect food images from post requests

Built With the help of:
1. Dataset preprocessing: Roboflow ->https://universe.roboflow.com/search?q=food
2. Hoped Dataset: https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/
3. Comet: Training Visualizer
4. calorieninjas: https://calorieninjas.com/api


> trained with
torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

