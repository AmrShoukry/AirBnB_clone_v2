#!/usr/bin/python3
""" 6-number_odd_or_even.py """

from flask import Flask, render_template
app = Flask(__name__)


from models import storage


@app.teardown_appcontext
def teardown(exception):
    """ remove sql session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def odd_even():
    """ 0.0.0.0:5000/hbnb/states_list """
    return render_template('7-states_list.html', data=storage.all('State').values())


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port='5000', debug=True)
