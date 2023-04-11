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

@app.route("/classify-error", methods=['POST', "GET"])
def upload_image_error():
    return render_template("classify-error.html")

@app.route("/get", methods=['GET', 'POST'])
def get_image():
    image = request.form.get('image')
    images.insert(0, image)
    picture = images[0]
    if (str(picture) != 'None'):
        with open("image.txt", "w") as image:
            image.write(f"static/css/images/{picture}")
        return redirect("/results")
    else:
        return redirect("/classify-error")

@app.route("/results")
def results():
    os.system('python3 dict.py')
    
    with open ("image.txt", "r") as output:
        image = output.read()
    with open ("prediction.txt", "r") as output:
        prediction = output.read()
    with open ("runtime.txt", "r") as output:
        runtime = output.read()

    return render_template("results.html", image=image, prediction=prediction, runtime=runtime)

app.run(port=5000)