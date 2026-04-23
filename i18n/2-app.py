#!/usr/bin/env python3
"""Flask app with Babel localization"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Babel configuration"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)

babel = Babel()


def get_locale():
    """Determine the best match with supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """Render index page"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(debug=True)
