#!/usr/bin/env python3
"""
Flask App.
"""
from flask import Flask, render_template, request
from flask import g
from os import getenv
from flask_babel import Babel, gettext
from datetime import datetime, timedelta
from pytz import timezone, UnknownTimeZoneError
import pytz
from flask_babel import format_datetime


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config Class."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app.config.from_object(Config)


@app.route('/')
def index():
    """Render index.html."""
    return render_template("index.html")


@babel.localeselector
def get_locale():
    """Determine the bestmatch languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    user_id = request.args.get('login_as')
    if user_id:
        locale = users[int(user_id)]['locale']
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Returns user dictionary or None"""
    try:
        user_id = request.args.get('login_as')
        return users[int(user_id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """Find a user if any, and set it as
    a global on flask.g.user. """
    g.user = get_user()
    zone = get_timezone()

    if not request.args.get("locale"):
        r_locale = get_locale()
        if r_locale == 'fr':
            g.timezone = format_datetime(datetime.now(
                pytz.timezone(zone)), 'dd MMM yyy à hh:mm:ss')
        else:
            g.timezone = format_datetime(datetime.now(
                pytz.timezone(zone)), 'MMM dd, yyy, hh:mm:ss a')
    else:
        loc = request.args.get("locale")
        if loc == 'fr':
            g.timezone = format_datetime(datetime.now(
                pytz.timezone(zone)), 'dd MMM yyy à hh:mm:ss')
        else:
            g.timezone = format_datetime(datetime.now(
                pytz.timezone(zone)), 'MMM dd, yyy, hh:mm:ss a')


@babel.timezoneselector
def get_timezone():
    """Determine the bestmatch Timezone."""
    timezone = request.args.get('timezone')
    try:
        if timezone in pytz.all_timezones and timezone is not None:
            return timezone
    except Exception:
        raise UnknownTimeZoneError

    user_id = request.args.get('login_as')
    if user_id is not None:
        timezone = users[int(user_id)]['timezone']
        if timezone is not None:
            try:
                if timezone in pytz.all_timezones and timezone is not None:
                    return timezone
            except Exception:
                raise UnknownTimeZoneError

    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
