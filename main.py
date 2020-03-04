"""
This project contains the boilerplate code necessary to make a Flask application, and connect it to your
already functional codebase.
"""

# Application requires the following
#   -   `flask.Flask` to build the Web Application.
#   -   `flask.render_template` to render HTML templates for displaying information to the user.
#   -   `flask.request` to access the content of the HTTP request being sent to the application.
#   -   `flask.abort` to deliver a 404 if an unsupported method is detected on our "/" route.
from flask import Flask, render_template, request, abort
import sys
sys.path.append("./src")


# Importing the my_code() function defined in `src.my_code`
from my_code import my_code
# Instantiating a Flask object, which acts as the core for our Web Application.
app = Flask(__name__)


# Defining a route for the Application. This means that when we go to http://localhost:8080/, this function is run.
# Definition of routes uses a Python decorator, which is essentially a function that adds behavior to another.
# This route can accept HTTP GET and HTTP POST requests. We can pivot functionality dependent on what we get.
@app.route("/", methods=["GET", "POST"])
# Defining the function that is run upon visiting http://localhost:8080/
def index():
    # If we get a HTTP GET request...
    if request.method == "GET":
        # We return our first html template, which just allows user input.
        return render_template("index.html")
    # If we get a HTTP POST request...
    elif request.method == "POST":
        # Store the user input form in a dictionary called user_input.
        # --> Casting to a dict is necessary as request.form is a Named Tuple. More complex to work with.
        # --> The `request` object stores everything about the incoming HTTP request.
        # --> `request.form` contains key-value pairs for all input fields in the HTML form.
        user_input = dict(request.form)
        # Run `my_code()` on the user input we took from the form.
        processed_user_input = my_code(str(user_input["input"][0]))
        # Return another, different template to output the result to the user.
        # --> Passing a keyword argument of processed_user_input lets us access the data in the template.
        return render_template("output.html", processed_user_input=processed_user_input)
    # If we get a HTTP request that is anything but POST or GET.
    else:
        # Abort, and serve a 404 error.
        abort(404)

# Run the Web Application on our local machine, on port 8080.
# --> Debug mode set to True will hot reload the application whenever changes are detected in the project.
app.run(host="0.0.0.0", port=8080, debug=True)