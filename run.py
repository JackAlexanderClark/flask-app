"""
Importing the flask class
Capital F for Flask because class name
Create an instance of the class
Naming convention for Flask 
"""
import os
from flask import Flask, render_template


app = Flask(__name__)       # Instance of Flask class


@app.route("/index")     # Decorators wrap around the function
def index():
    return render_template("index.html")


@app.route("/about")        # Routing to about.html
def about():        # View function must match url_for text
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")fffc 
def careers():
    return render_template("careers.html")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),       # Using os module to .get the 'IP' environment
        port=int(os.environ.get("PORT", "5000")), 
        debug=True)     # debug=True allows easier debug later in dev
                        # must not be used in production code as security flaw



    


"""
Notes: 
- Flask and Django frameworks allow us to reuse as much code as possible.
- Resusing templates and {%%} 
"""