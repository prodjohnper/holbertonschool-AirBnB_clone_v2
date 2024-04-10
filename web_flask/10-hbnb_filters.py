#!/usr/bin/python3
'''
    Script that starts a Flask web application
'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


# Route /hbnb_filters: display a HTML page
@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''
        Returns a string to the route /hbnb_filters of the web application
    '''
    states = storage.all('State')
    cities = storage.all('City')
    amenities = storage.all('Amenity')

    # Render the HTML template
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


# app.teardown_appcontext: Remove the current SQLAlchemy Session
@app.teardown_appcontext
def teardown_db(exception):
    '''
        Method to remove the current SQLAlchemy Session
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
