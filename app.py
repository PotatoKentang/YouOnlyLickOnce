import requests
from flask import Flask, request, jsonify
from train.train import predict
from utility.links import get_nutrition_by_id
from utility.error import error_handler
from werkzeug.utils import secure_filename
from utility.get_nutrients import get_nutrients
from utility.allowed_files import allowed_file
import os
UPLOAD_FOLDER = '/data/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from dotenv import load_dotenv
load_dotenv()


@app.route("/")
def home():
    return "Hello World!"

@app.route("/get_nutrients")
def get_nutrients_from_query():
    status_code,data = get_nutrients("apple")
    if status_code != requests.codes.OK:
        return error_handler("error getting data")
    return data

@app.route("/food", methods=["POST"])
def get_food_image_from_post():
    if request.method != 'POST':
        return
    if 'file' not in request.files:
        return error_handler("no file part")
    fileUploaded = request.files['file']
    if fileUploaded.filename == '':
        return error_handler("no selected file")
    if not allowed_file(fileUploaded.filename):
        return error_handler("file not allowed")
    filename = secure_filename(fileUploaded.filename)
    fullpath = os.path.normpath(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    os.makedirs(os.path.dirname(fullpath), exist_ok=True)
    fileUploaded.save(fullpath)
    img,label = predict(fullpath)
    return jsonify({"label":label,"image":img}), 200


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0",port=8080)
