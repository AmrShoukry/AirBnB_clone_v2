#!/usr/bin/python3
""" 8-cities_by_states.py """

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ remove sql session """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    """ 0.0.0.0:5000/hbnb/cities_by_states """
    state_objects = storage.all('State').values()
    states = sorted(state_objects, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
