#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ Babel configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """ Home page """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """ doc doc doc """
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """Get user"""
    user_id = request.args.get('login_as')
    if user_id is not None and user_id in users:
        return users[user_id]
    return None


@app.before_request
def before_request():
    """Before request"""
    user = get_user()
    g.user = user


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
