#!/usr/bin/python3
""""
A script that starts Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello "HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB
    """
    return "HBNB"


@app.route('/c/(<text>)', strict_slashes=False)
def c_is_text(text):
    """ Displays "C" followed by value of text variable
    """
    return "C{}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays python followed by value of text variable
    replaces underscore with a space
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
