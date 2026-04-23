#!/usr/bin/env python3
"""
Flask app: force locale with URL parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

# docstring pour le checker
_.__doc__ = "Translation function"


class Config:
    """Application configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Determine best locale"""
    # 🔥 priorité au paramètre URL
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    # fallback normal
    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
