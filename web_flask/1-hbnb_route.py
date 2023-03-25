#!/usr/bin/python3
"""
STARTS A FLASK WEB APPLICATION
LISTENING ON 0.0.0.0, PORT 5000
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ DISPLAYS 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ DISPLAYS 'HBNB'. """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0")

