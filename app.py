from flask import Flask
from flask import render_template, Response, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

