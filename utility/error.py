from flask import jsonify

def error_handler(error):
    return jsonify({"error": str(error)}), 400