#!/usr/bin/python3
""" 0-hello_route.py """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ 0.0.0.0:5000/ """
    return ("Hello HBNB!")


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True)
