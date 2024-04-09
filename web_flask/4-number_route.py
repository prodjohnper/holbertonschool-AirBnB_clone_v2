#!/usr/bin/python3
'''
    Script that starts a Flask web application
'''
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
