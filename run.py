"""
Importing the flask class
Capital F for Flask because class name
Create an instance of the class
Naming convention for Flask 
"""
import os
from flask import Flask, render_template


app = Flask(__name__)

# Adding an additional argument into return statement
@app.route("/")
def index():
    return render_template("index.html", page_title="About")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)


"""
Notes: 
- Flask and Django frameworks allow us to reuse as much code as possible.
- Resusing templates and {%%} 
"""