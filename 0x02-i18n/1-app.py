#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Config class """
    LANGUAGES = ["en", "fr"]


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Home page """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
