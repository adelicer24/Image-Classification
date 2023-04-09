from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

images = []

from werkzeug.utils import secure_filename



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify", methods=['POST', "GET"])
def upload_image():
    return render_template("classify.html")

@app.route("/get", methods=['GET', 'POST'])
def get_image():
    image = request.form.get('image')
    images.insert(0, image)
    picture = images[0]
    with open("image.txt", "w") as image:
        image.write(f"static/css/images/{picture}")
    return redirect("/results")

@app.route("/results")
def results():
    os.system('python3 test.py')
    with open ("prediction.txt", "r") as output:
        prediction = output.read()
    with open ("image.txt", "r") as output:
        image = output.read()

    return render_template("results.html", image=image, prediction=prediction)

app.run(port=5000)