#!/usr/bin/python3
"""
An application that starts Flask Web application
/ displays Hello HBNB!"
/hbnb displays HBNB
/c/<text> displays C
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB!"
    """
    return "HBNBN!"


@app.route('/c/<text>', strict_slashes=False)
def c_is_text(text):
    """
    displays "C" followed by the value of the text variable
    replaces the underscore_symbol with a space )
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
