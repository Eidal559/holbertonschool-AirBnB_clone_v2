#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Route to display a HTML page with the list of all State objects present in DBStorage
    """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)

    return render_template('9-states.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def state_cities_list(id):
    """
    Route to display a HTML page with the list of City objects linked to the State with the given id
    """
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Teardown method to remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
