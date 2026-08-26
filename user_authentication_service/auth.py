#!/usr/bin/env python3
"""Authentication service module."""

import uuid
from typing import Optional

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


def _generate_uuid() -> str:
    """Generate and return a UUID string."""
    return str(uuid.uuid4())


class Auth:
    """Manage user authentication."""

    def __init__(self):
        """Initialize the authentication service."""
        self._db = DB()

    def register_user(
        self,
        email: str,
        password: str
    ) -> User:
        """Register a new user."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(
                password
            )

            return self._db.add_user(
                email,
                hashed_password
            )

        raise ValueError(
            "User {} already exists".format(email)
        )

    def valid_login(
        self,
        email: str,
        password: str
    ) -> bool:
        """Validate an email and password."""
        try:
            user = self._db.find_user_by(
                email=email
            )
        except NoResultFound:
            return False

        hashed_password = user.hashed_password

        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode(
                "utf-8"
            )

        try:
            return bcrypt.checkpw(
                password.encode("utf-8"),
                hashed_password
            )
        except (TypeError, ValueError):
            return False

    def create_session(
        self,
        email: str
    ) -> Optional[str]:
        """Create a session for a user."""
        try:
            user = self._db.find_user_by(
                email=email
            )
        except NoResultFound:
            return None

        session_id = _generate_uuid()

        self._db.update_user(
            user.id,
            session_id=session_id
        )

        return session_id

    def get_user_from_session_id(
        self,
        session_id: str
    ) -> Optional[User]:
        """Return a user matching a session ID."""
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(
                session_id=session_id
            )
        except NoResultFound:
            return None

    def destroy_session(
        self,
        user_id: int
    ) -> None:
        """Destroy a user's session."""
        self._db.update_user(
            user_id,
            session_id=None
        )

    def get_reset_password_token(
        self,
        email: str
    ) -> str:
        """Generate a password reset token."""
        try:
            user = self._db.find_user_by(
                email=email
            )
        except NoResultFound as error:
            raise ValueError from error

        reset_token = _generate_uuid()

        self._db.update_user(
            user.id,
            reset_token=reset_token
        )

        return reset_token

    def update_password(
        self,
        reset_token: str,
        password: str
    ) -> None:
        """Update a user's password."""
        try:
            user = self._db.find_user_by(
                reset_token=reset_token
            )
        except NoResultFound as error:
            raise ValueError(
                "Invalid reset token"
            ) from error

        hashed_password = _hash_password(
            password
        )

        self._db.update_user(
            user.id,
            hashed_password=hashed_password,
            reset_token=None
        )
