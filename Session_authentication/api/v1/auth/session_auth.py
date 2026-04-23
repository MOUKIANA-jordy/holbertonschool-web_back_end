#!/usr/bin/env python3
"""Session authentication module"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session authentication class"""

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """Determine if auth is required"""
        return super().require_auth(path, excluded_paths)
