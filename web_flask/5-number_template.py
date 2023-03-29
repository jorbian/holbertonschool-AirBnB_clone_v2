#!/usr/bin/python3
"""
STARTS A FLASK WEB APPLICATION
LISTENING ON 0.0.0.0, PORT 5000
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ DISPLAYS 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ DISPLAYS 'HBNB'. """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ DISPLAYS 'C' FOLLOWED BY THE VALUE OF <text>. """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ DISPLAYS 'Python' FOLLOWED BY THE VALUE OF <text> """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ DISPLAYS 'n is a number' ONLY IF <n> IS AN INTEGER """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """  DISPLAYS HTML PAGE  ONLY IF <n> IS AN INTEGER """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
