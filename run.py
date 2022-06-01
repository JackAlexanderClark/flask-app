"""
Importing the flask class
Capital F for Flask because class name
Create an instance of the class
Naming convention for Flask 
"""
import os
from flask import Flask


app = Flask(__name__)       # Instance of Flask class


@app.route("/")     # Decorators wrap around the function
def index():
    return "HELLO WORLD IT IS I FLASK"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),       # Using os module to .get the 'IP' environment
        port=int(os.environ.get("PORT", "5000")), 
        debug=True)     # debug=True allows easier debug later in dev
    ) 
