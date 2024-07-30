#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Home page """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Gwt locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
