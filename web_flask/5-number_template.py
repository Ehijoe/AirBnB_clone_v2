#!/usr/bin/python3
"""Templates."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Handle requests."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handle requests."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text: str):
    """Handle requests."""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text: str):
    """Handle requests."""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    """Handle requests."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbers_template(n):
    """Handle requests."""
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
