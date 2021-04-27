#!/usr/bin/env python3
"""
Flask App.
"""
from flask import Flask, render_template, request
from os import getenv
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config Class."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Render index.html."""
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """Determine the bestmatch languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
