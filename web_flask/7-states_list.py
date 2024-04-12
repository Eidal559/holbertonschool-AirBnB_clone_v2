#!/usr/bin/python3
"""Flask web application that displays a list of State objects from storage."""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """Display a list of all State objects sorted by name (A-Z)."""
    states = storage.all(State)  # Fetch all State objects from storage
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    # Create the HTML template with the list of states
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def close_storage(exception):
    """Close the storage connection after each request."""
    storage.close()


if __name__ == "__main__":
    # Start the Flask application
    app.run(host="0.0.0.0", port=5000)
