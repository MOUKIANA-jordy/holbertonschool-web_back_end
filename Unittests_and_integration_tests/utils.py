#!/usr/bin/env python3
"""Utilitaires génériques pour le client github org.
"""
demandes d'importation
à partir de functools importer des wraps
en tapant import (
    Cartographie,
    Séquence,
    N'importe lequel,
    Dict,
    Appelable,
)

__tous__ = [
    "access_nested_map",
    "get_json",
    "mémoriser",
]


def access_nested_map(nested_map : mappage, chemin : séquence) -> Tout :
    """Accédez à la carte imbriquée avec le chemin clé.
    Paramètres
    ----------
    nested_map : cartographie
        Une carte imbriquée
    chemin : Séquence
        une séquence de clés représentant un chemin vers la valeur
    Exemple
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    pour la clé dans le chemin :
        sinon isinstance(nested_map, Mapping) :
            générer KeyError(clé)
        nested_map = nested_map[clé]

    renvoyer nested_map


def get_json(url: str) -> Dict:
    """Obtenir JSON à partir d'une URL distante.
    """
    réponse = requêtes.get(url)
    renvoyer response.json()


def memoize(fn: Callable) -> Callable:
    """Décorateur pour mémoriser une méthode.
    Exemple
    -------
    classe MaClasse :
        @memoize
        def a_method(self) :
            print("une_méthode appelée")
            retour 42
    >>> mon_objet = MaClasse()
    >>> mon_objet.une_méthode
    une_méthode appelée
    42
    >>> mon_objet.une_méthode
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def mémorisé(soi) :
        """"enveloppements mémorisés"""
        sinon hasattr(self, attr_name) :
            setattr(self, attr_name, fn(self))
        renvoie getattr(self, attr_name)

    propriété de retour (mémorisée)
