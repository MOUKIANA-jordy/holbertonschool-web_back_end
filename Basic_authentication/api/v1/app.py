#!/usr/bin/env python3
"""Route module for the API"""

from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from models.user import User

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

# 🔐 Charger Auth selon variable d'environnement
if getenv("AUTH_TYPE") == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """Filter all incoming requests"""
    if auth is None:
        return

    excluded_paths = [
        "/api/v1/status/",
        "/api/v1/unauthorized/",
        "/api/v1/forbidden/"
    ]

    # Vérifie si la route nécessite auth
    if not auth.require_auth(request.path, excluded_paths):
        return

    # Vérifie header Authorization
    if auth.authorization_header(request) is None:
        abort(401)

    # Vérifie utilisateur
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    try:
        User.load_from_file()
        print("Utilisateurs chargés avec succès.")
    except Exception as e:
        print(f"Impossible de charger les utilisateurs : {e}")

    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
