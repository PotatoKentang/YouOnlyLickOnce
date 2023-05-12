import requests
from flask import Flask, request, jsonify
from utility.error import error_handler
from werkzeug.utils import secure_filename
from core.get_ingredients_list import get_ingredients_list, get_ingredients_list_by_id
from core.get_prediction_image import predict_image
from core.get_nutrients import get_nutrients
from utility.allowed_files import allowed_file
from flask_cors import CORS
import os
UPLOAD_FOLDER = 'data/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from dotenv import load_dotenv
load_dotenv()
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/",methods=["GET","POST"])
def home():
    return jsonify({"message": "Welcome to the API"}), 200

@app.route("/list_of_ingredients",methods=["POST"])
def fetch_ingredients_from_searchbar():
    print("ingredients from searchbar called")
    if request.method != 'POST':
        return
    if 'query' not in request.form:
        return error_handler("no query part")
    query = request.form['query']
    data,status_code = get_ingredients_list(query)
    if status_code != requests.codes.OK:
        return error_handler("error getting data")
    return jsonify(data), status_code


@app.route("/list_of_ingredients/<id>",methods=["POST"])
def fetch_ingredients_information_by_id(id):
    print("ingredients from id called")
    if request.method != 'POST':
        return
    amount = request.form['amount']
    unit = request.form['unit']
    data,status_code = get_ingredients_list_by_id(id,amount,unit)
    if status_code != requests.codes.OK:
        return error_handler("error getting data")
    return jsonify(data), status_code


@app.route("/get_nutrients",methods=["POST"])
def get_nutrients_from_query():
    if request.method != 'POST':
        return
    if 'query' not in request.form:
        return error_handler("no query part")
    query = request.form['query']
    data,status_code = get_nutrients(query)
    if status_code != requests.codes.OK:
        return error_handler("error getting data")
    return jsonify(data), status_code

@app.route("/predict_image", methods=["POST"])
def get_food_image_from_post():
    if request.method != 'POST':
        return
    if 'image' not in request.files:
        return error_handler("no file part")
    fileUploaded = request.files['image']
    if fileUploaded.filename == '':
        return error_handler("no selected file")
    if not allowed_file(fileUploaded.filename):
        return error_handler("file not allowed")
    filename = secure_filename(fileUploaded.filename)
    fullpath = os.path.normpath(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    os.makedirs(os.path.dirname(fullpath), exist_ok=True)
    fileUploaded.save(fullpath)
    img,label = predict_image(fullpath)
    return jsonify({"label":label,"image":img}), 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0",port=8080)
