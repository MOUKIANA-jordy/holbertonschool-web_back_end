#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests unitaires pour GithubOrgClient."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Vérifie que has_license retourne la bonne valeur booléenne."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected
        )
