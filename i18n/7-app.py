#!/usr/bin/env python3
"""Flask application with locale and timezone selection."""

from datetime import datetime
from typing import Optional

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel


class Config:
    """Configure the supported languages and default timezone."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


users = {
    1: {
        "name": "Balou",
        "locale": "fr",
        "timezone": "Europe/Paris",
    },
    2: {
        "name": "Beyonce",
        "locale": "en",
        "timezone": "US/Central",
    },
    3: {
        "name": "Spock",
        "locale": "kg",
        "timezone": "Vulcan",
    },
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London",
    },
}


def get_user() -> Optional[dict]:
    """Return the user identified by the login URL parameter."""
    login_as = request.args.get("login_as")

    if login_as is None:
        return None

    try:
        user_id = int(login_as)
    except (TypeError, ValueError):
        return None

    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """Store the current user in Flask's global request object."""
    g.user = get_user()


def get_locale() -> str:
    """Determine the best locale for the current request."""
    locale = request.args.get("locale")

    if locale in app.config["LANGUAGES"]:
        return locale

    if g.user:
        user_locale = g.user.get("locale")

        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    return request.accept_languages.best_match(
        app.config["LANGUAGES"]
    )


def get_timezone() -> str:
    """Determine and validate the timezone for the current request."""
    timezone = request.args.get("timezone")

    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        user_timezone = g.user.get("timezone")

        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return "UTC"


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """Render the translated home page with the current local time."""
    timezone = get_timezone()
    current_time = datetime.now(
        pytz.timezone(timezone)
    ).strftime("%b %d, %Y, %I:%M:%S %p")

    return render_template(
        "7-index.html",
        current_time=current_time,
    )


if __name__ == "__main__":
    app.run()
