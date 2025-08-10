#!/usr/bin/env python3
"""Un client d'organisation GitHub
"""
en tapant import (
    Liste,
    Dict,
)

à partir de l'importation d'utilitaires (
    obtenir_json,
    access_nested_map,
    mémoriser,
)


classe GithubOrgClient :
    """Un client d'organisation Githib
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> Aucun:
        Méthode d'initialisation de GithubOrgClient
        self._org_name = nom_organisation

    @memoize
    def org(self) -> Dict:
        """Memoize org"""
        retourner get_json(self.ORG_URL.format(org=self._org_name))

    @propriété
    def _public_repos_url(self) -> str:
        """URL des dépôts publics"""
        retour self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        « Charge utile des dépôts Memoize »
        retourner get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> Liste[str]:
        """Dépôts publics"""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] pour repo dans json_payload
            si la licence est None ou self.has_license(repo, license)
        ]

        renvoyer public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Statique : has_license"""
        assert license_key n'est pas None, "license_key ne peut pas être None"
        essayer:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        sauf KeyError :
            renvoie Faux
        retourner has_license
