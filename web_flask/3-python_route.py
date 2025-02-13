#!/usr/bin/python3
""" 3-python_route.py """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ 0.0.0.0:5000/ """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ 0.0.0.0:5000/hbnb """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ 0.0.0.0:5000/hbnb/c/<text> """
    return (f"C {text.replace('_', ' ')}")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ 0.0.0.0:5000/hbnb/python/<text> """
    return (f"Python {text.replace('_', ' ')}")


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
