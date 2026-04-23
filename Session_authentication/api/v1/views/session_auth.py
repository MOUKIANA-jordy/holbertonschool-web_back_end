#!/usr/bin/env python3
"""Session authentication views"""

from flask import request, jsonify, abort, make_response
from models.user import User
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handle login and create session"""

    email = request.form.get('email')
    password = request.form.get('password')

    # 🔴 email missing
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    # 🔴 password missing
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    # 🔍 search user
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # 🔴 wrong password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # 🔥 créer session
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    # 📦 réponse JSON
    response = make_response(jsonify(user.to_json()))

    # 🍪 set cookie
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
