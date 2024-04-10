#!/usr/bin/python3
'''
    Script that starts a Flask web application
'''
from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)


# Route /: display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello():
    '''
        Returns a string to the root route / of the web application
    '''
    return 'Hello HBNB!'


# Route /hbnb: display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
        Returns a string to the route /hbnb of the web application
    '''
    return 'HBNB'


# Route /c/<text>: display "C " followed by the value of the text variable
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''
        Returns a string to the route /c/<text> of the web application,
        that exchanges text for the value of the text variable
    '''
    return 'C {}'.format(text.replace('_', ' '))


# Route /python/(<text>): display "Python " followed by the value of the text variable
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    '''
        Returns a string to the route /python/<text> of the web application,
        that exchanges text for the value of the text variable, has def value
    '''
    return 'Python {}'.format(text.replace('_', ' '))

    # defaults to 'is cool' if no text is given


# Route /number/<n>: display "n is a number" only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
        Returns a string to the route /number/<n> of the web application,
        that exchanges n for the value of the n variable, only if n is an int
    '''
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        pass  # will not return anything if n is not an int, displays 404 error page


# Route /number_template/<n>: display an HTML page only if n is an integer
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
        Returns a string to the route /number_template/<n> of the web application,
        that exchanges n for the value of the n variable, only if n is an int
    '''
    if isinstance(n, int):
        # renders template with n
        return render_template('5-number.html', number=n)
    else:
        pass  # will not return anything if n is not an int, displays 404 error page


# Route /number_odd_or_even/<n>: display an HTML page only if n is an integer
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''
        Returns a string to the route /number_odd_or_even/<n> of the web application,
        that exchanges n for the value of the n variable, only if n is an int
    '''

    # Determines if n is odd or even
    number_odd_or_even = 'even' if n % 2 == 0 else 'odd'

    if isinstance(n, int):
        # renders template with n
        return render_template('6-number_odd_or_even.html', number=n, number_odd_or_even=number_odd_or_even)
    else:
        pass  # will not return anything if n is not an int, displays 404 error page


# Teardown: closes the current SQLAlchemy Session
@app.teardown_appcontext
def teardown_db(exception):
    '''
        Closes the current SQLAlchemy Session
    '''
    storage.close()


# Route /states_list: display an HTML page
@app.route('/states_list', strict_slashes=False)
def states_list():
    '''
        Returns a string to the route /states_list of the web application
    '''
    # renders template with states
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


# Route /cities_by_states: display an HTML page
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''
        Returns a string to the route /cities_by_states of the web application
    '''
    # renders template with states
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


# Route /states: display an HTML page
@app.route('/states', strict_slashes=False)
def states():
    '''
        Returns a string to the route /states of the web application
    '''
    # renders template with states
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


# Route /states/<id>: display an HTML page
@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    '''
        Returns a string to the route /states/<id> of the web application
    '''
    if id:
        try:
            state = storage.all(State)[f'State.{id}']
            return render_template('9-states.html', state=state, id=id,
                                   header='States')
        except KeyError:
            return render_template('9-states.html', error='Not found!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
