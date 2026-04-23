#!/usr/bin/env python3
"""Auth module for managing API authentication"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # rendre path slash tolerant
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Return the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user"""
        return None
