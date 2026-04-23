#!/usr/bin/env python3
"""Auth module for managing API authentication"""

from typing import List, TypeVar
from os import getenv


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Return the authorization header"""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user"""
        return None

    def session_cookie(self, request=None):
        """Return a cookie value from a request"""
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)
