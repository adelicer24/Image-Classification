from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify")
def classify():
    return render_template("classify.html")

@app.route("/results")
def results():
    return render_template("results.html")