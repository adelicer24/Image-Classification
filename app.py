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
    if request.method == "POST":

        image = request.files['file']

        if image.filename == '':
            return redirect(request.url)
        
        filename = secure_filename(image.filename)

        basedir = os.path.abspath(os.path.dirname(__file__))
        image.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"], filename))

        return render_template("results.html", filename=filename)

    return render_template("classify.html")

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename = '/images/'+filename, code=301))

@app.route("/results")
def results():
    return render_template("results.html")

app.run(port=5000)