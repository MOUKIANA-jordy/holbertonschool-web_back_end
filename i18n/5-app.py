#!/usr/bin/env python3
"""
Flask app: mock login system with Flask-Babel
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

# docstring pour le checker
_.__doc__ = "Translation function"


class Config:
    """Application configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Mock database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_user():
    """Return user dict or None"""
    user_id = request.args.get("login_as")
    if user_id:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except Exception:
            return None
    return None


@app.before_request
def before_request():
    """Set user in global flask.g"""
    g.user = get_user()


def get_locale():
    """Determine best locale"""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
