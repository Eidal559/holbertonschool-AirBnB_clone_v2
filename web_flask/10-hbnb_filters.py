#!/usr/bin/python3
"""Flask web application that displays States, Cities, and Amenities with filters."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/hbnb_filters")
def hbnb_filters():
    """Display an HTML page with filters for States, Cities, and Amenities."""
    # Fetch and sort states and amenities by name
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    # Sort the lists by name
    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    
    # Load cities of each state and sort them by name
    for state in sorted_states:
        # If using DBStorage, use cities relationship
        # Otherwise, use public getter method cities
        if getenv('HBNB_TYPE_STORAGE') == "db":
            cities = state.cities
        else:
            cities = state.cities()
        state.cities = sorted(cities, key=lambda city: city.name)

    # Render the HTML template with the states and amenities data
    return render_template("10-hbnb_filters.html", states=sorted_states, amenities=sorted_amenities)

@app.teardown_appcontext
def close_storage(exception):
    """Close the storage session after each request."""
    storage.close()

if __name__ == "__main__":
    # Start the Flask application
    app.run(host="0.0.0.0", port=5000)
