#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Optional


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a salt.

    Args:
        password (str): Plain text password.

    Returns:
        bytes: Salted hash of the password.
    """
    # bcrypt.hashpw attend des bytes, donc on encode le mot de passe en UTF-8
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        Raises ValueError if user already exists.
        """
        try:
            # Vérifier si un utilisateur existe déjà
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hachage du mot de passe
            hashed_pwd = _hash_password(password)
            # Ajouter l'utilisateur à la base
            return self._db.add_user(email, hashed_pwd.decode("utf-8"))

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates if a given email and password correspond to a valid user.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """
        Create a session ID for the user identified by email.
        Return the session ID as a string, or None if user not found.
        """
        try:
            # 1. Trouver l'utilisateur par email
            user = self._db.find_user_by(email=email)
        except Exception:
            return None

        # 2. Générer un nouvel identifiant de session
        session_id = _generate_uuid()

        # 3. Mettre à jour l'utilisateur avec le nouvel ID de session
        self._db.update_user(user.id, session_id=session_id)

        # 4. Retourner l'ID de session
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        Retrieve a user by their session_id.

        Args:
            session_id (str): The session ID to look up.

        Returns:
            User | None: The corresponding User object, or None if not found.
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def update_password(self, reset_token: str, password: str) -> None:
        """ Updates a user's password based on a reset token.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)

        except NoResultFound:
            raise ValueError("Invalid reset token")

    def destroy_session(self, user_id: int) -> None:
        """ Destroys a user's session by setting their session ID to None.
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Generates a reset password token for a user with the given email.
        """
        token = _generate_uuid()

        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=token)
            return token

        except NoResultFound:
            raise ValueError


def _generate_uuid() -> str:
    """
    Generate a new UUID and return it as a string.
    Private function: should not be used outside auth.py
    """
    return str(uuid.uuid4())
