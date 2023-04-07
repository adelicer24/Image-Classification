from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.config['IMAGE_UPLOADS'] = '/Users/Alexd/OneDrive/Desktop/CSCI-200/Junior IS Software/Image-Classification/static/css/images'

from werkzeug.utils import secure_filename

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify", methods=['POST', "GET"])
def upload_image():
    return render_template("classify.html")

@app.route("/results")
def results():
    os.system('python3 test.py')
    with open ("output.txt", "r") as output:
        accuracy = output.read()

    return render_template("results.html", accuracy=accuracy)

app.run(port=5000)