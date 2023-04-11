# This python file is the web application part of my software which
# contains all the routes to the different html pages

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# This array will hold the name of the image path of the image that
# is chosen by the user to test on the model
images = []

# This is the home page that will first appear to the user
@app.route("/")
def index():
    return render_template("index.html")

# This is the classify page which will allow the user to choose an
# image to test in the model
@app.route("/classify", methods=['POST', "GET"])
def upload_image():
    return render_template("classify.html")

# This is the classify page which only appears if the user does not
# select and image
@app.route("/classify-error", methods=['POST', "GET"])
def upload_image_error():
    return render_template("classify-error.html")

# This function retieves the user's selected image and records the
# image path in a txt file. If an image is selected, the user will be
# redirected to the results page. If an image is not selected, the
# user will be redirected back to the classify page with an error
# message
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

# This is the results page which will display the image that was 
# picked by the user, the predicted class that the image is in, and
# the runtime of the model when predicting the image.
# The information is retrieved by calling the python file dict.py 
# which will write the prediction and runtime in txt files. The image
# path is also retrieved from a txt file which is recorded when the 
# user picks an image.
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