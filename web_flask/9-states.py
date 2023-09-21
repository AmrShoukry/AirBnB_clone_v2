#!/usr/bin/python3
""" 9-states.py """

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ remove sql session """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ 0.0.0.0:5000/hbnb/states """
    state_objects = storage.all('State').values()
    states = sorted(state_objects, key=lambda state: state.name)
    return render_template('9-states.html', data=states, type='states')


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ 0.0.0.0:5000/hbnb/states/<id> """
    state_objects = storage.all('State').values()
    states = sorted(state_objects, key=lambda state: state.name)
    for state in states:
        if state.id == id:
            return render_template('9-states.html', data=state, type='state')
    return render_template('9-states.html', data=None, type='NULL')


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
