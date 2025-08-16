#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests unitaires pour GithubOrgClient.public_repos"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Tester que public_repos renvoie la bonne liste de dépôts"""

        # Faux payload simulant la réponse de l’API
        payload_faux = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = payload_faux

        # Patch de la propriété _public_repos_url
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_repos_url:
            mock_repos_url.return_value = "http://faux-url.com"

            client = GithubOrgClient("test_org")
            resultat = client.public_repos()

            # On vérifie que la liste renvoyée est correcte
            attendu = ["repo1", "repo2", "repo3"]
            self.assertEqual(resultat, attendu)

            # Vérifie que get_json a été appelé une seule fois
            mock_get_json.assert_called_once_with("http://faux-url.com")

            # Vérifie que la propriété a été utilisée une seule fois
            mock_repos_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()
