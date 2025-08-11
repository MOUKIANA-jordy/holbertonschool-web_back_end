#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        # Valeur de retour simulée par get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        client = GithubOrgClient("test_org")

        # Mock de la propriété _public_repos_url
        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=unittest.mock.PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://fakeurl.com/repos"

            # Appel de la méthode à tester
            repos = client.public_repos()

            # Vérifications
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://fakeurl.com/repos")

if __name__ == "__main__":
    unittest.main()
