#!/usr/bin/env python3
"""Flask app with Babel localization"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"


app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Select best language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render template"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
