#!/usr/bin/python3
"""FLASK FRAMEWORK"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    """Return Hello world"""
    return f"Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return hbnb"""
    return f"HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """show the script"""
    return f'C {text.replace("_", " ")}'

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    """show the script"""
    return f'Python {text.replace("_", " ")}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
