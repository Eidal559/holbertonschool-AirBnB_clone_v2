#!/usr/bin/python3
"""This module creates a local server with flask with 2 routes"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from os import getenv


app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


@app.route("/states_list")
def state_list():
    """This method fetchs data from storage to display the list of states"""

    states = storage.all()
    sorted_data = sorted(states.values(), key=lambda state: state.name)
    for state in sorted_data:
        state.id = str(state.id)
        state.name = str(state.name)
    return render_template("7-states_list.html", states=sorted_data)


@app.teardown_appcontext
def close_storage():
    """This method closes storage session if storage db"""

    if getenv('HBNB_TYPE_STORAGE') == "db":
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
