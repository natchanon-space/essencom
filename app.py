from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/content")
def content():
    return render_template("content.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/video", methods=["GET", "POST"])
def video():
    return render_template("video.html")