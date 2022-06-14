"""
Importing the flask class
Capital F for Flask because class name
Create an instance of the class
Naming convention for Flask 
"""
import os
import json
from flask import Flask, render_template


app = Flask(__name__)

# Adding an additional argument into return statement
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []

    # Using a with block, "r" means read-only, assigning to variable json_data
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

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