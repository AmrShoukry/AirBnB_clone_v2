#!/usr/bin/python3
""" 7-states_list.py """

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ remove sql session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    """ 0.0.0.0:5000/hbnb/states_list """
    state_objects = storage.all('State').values()
    data = sorted(state_objects, key=lambda state: state.name)
    return render_template('7-states_list.html', data=data)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
