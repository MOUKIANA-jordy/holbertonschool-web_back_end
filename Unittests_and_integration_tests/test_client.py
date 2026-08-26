#!/usr/bin/env python3
"""Unit tests for the Github organization client."""

import unittest
from unittest.mock import patch, PropertyMock

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class."""

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that org returns the expected payload."""
        expected_payload = {
            "login": org_name,
            "repos_url": (
                "https://api.github.com/orgs/"
                "{}/repos".format(org_name)
            ),
        }

        mock_get_json.return_value = expected_payload
        github_client = GithubOrgClient(org_name)

        self.assertEqual(
            github_client.org,
            expected_payload
        )

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(
                org_name
            )
        )

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the mocked repository URL."""
        expected_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_url}

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = payload
            github_client = GithubOrgClient("google")

            self.assertEqual(
                github_client._public_repos_url,
                expected_url
            )

            mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
