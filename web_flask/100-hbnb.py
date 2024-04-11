#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Route to display the hbnb HTML page."""
    # Retrieve all state, amenity, and place objects from storage
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)

    # Load all cities for each state
    for state in states:
        if storage.get_type() == 'db':
            # Use relationship attribute for DBStorage
            state.cities = state.cities
        else:
            # Use public getter method for FileStorage
            state.cities = state.cities
    
    # Render the HTML page
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)

if __name__ == '__main__':
    # Start Flask app listening on 0.0.0.0 port 5000
    app.run(host='0.0.0.0', port=5000)
