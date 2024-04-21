#!/usr/bin/python3
"""FLASK FRAMEWORK"""
from flask import Flask, render_template

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


@app.route('/python/<text>', strict_slashes=False)
def py(text):
    """show the script"""
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """show the script"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """show the script"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """show the script"""
    className = ""
    if n % 2 == 0:
        className = "odd"
    else:
        className = "even"
    return render_template("6-number_odd_or_even.html", n=n,
                           className=className)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
