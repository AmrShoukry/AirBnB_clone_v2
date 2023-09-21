#!/usr/bin/python3
""" 5-number_template.py """

from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ 0.0.0.0:5000/hbnb/number/<n> """
    return (f"{n} is a number")


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ 0.0.0.0:5000/hbnb/number_template/<n> """
    return render_template('5-number.html', n=n)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
