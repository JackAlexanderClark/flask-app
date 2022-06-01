"""
Importing the flask class
Capital F for Flask because class name
Create an instance of the class
Naming convention for Flask 
"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "HELLO WORLD IT IS I FLASK"
