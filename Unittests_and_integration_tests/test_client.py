#!/usr/bin/env python3
import unittest
from unittest.mock import patch
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos avec mocks sur get_json et _public_repos_url."""
        # 1. Payload fictif
        payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = payload

        # 2. URL fictive pour _public_repos_url
        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=unittest.mock.PropertyMock) as mock_url:
            mock_url.return_value = "http://fake-url.com"

            # 3. Exécuter la méthode
            client = GithubOrgClient("test_org")
            result = client.public_repos()

            # 4. Vérifier le résultat
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # 5. Vérifier que _public_repos_url a été appelé une fois
            mock_url.assert_called_once()

            # 6. Vérifier que get_json a été appelé une fois
            mock_get_json.assert_called_once_with("http://fake-url.com")
