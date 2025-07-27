Project README
📘 Objectif
Ce projet a pour but de mettre en œuvre les meilleures pratiques autour de la gestion des données personnelles (PII) dans une application Python. À la fin, vous serez capable de :

Identifier les informations personnelles identifiables (PII).

Masquer ces données sensibles dans les logs via une fonction utilitaire.

Chiffrer des mots de passe avec bcrypt et valider un mot de passe en clair.

Se connecter à une base de données MySQL en utilisant des variables d’environnement pour les informations sensibles.

📁 Structure du Projet
Le projet comprend plusieurs modules Python, chacun dédié à une tâche spécifique :

filtered_logger.py

filter_datum(fields, redaction, message, separator) : masque via regex les valeurs des champs sensibles dans une ligne de log. En moins de 5 lignes, en utilisant re.sub.

RedactingFormatter : classe personnalisée dérivée de logging.Formatter. Elle accepte une liste de fields, utilise filter_datum dans sa méthode format pour remplacer les valeurs PII par un texte de redaction (***), sans réimplementer manuellement le format.

Fonction get_logger() : fournit un objet logging.Logger nommé "user_data" :

Niveau maximal : INFO

Pas de propagation vers d’autres loggers

Un StreamHandler avec notre RedactingFormatter

Utilise une constante PII_FIELDS contenant les 5 champs choisis comme sensibles (parmi ceux du fichier user_data.csv).

Fonction get_db() : se connecte à une base MySQL en utilisant :

os.environ pour lire : PERSONAL_DATA_DB_USERNAME, PERSONAL_DATA_DB_PASSWORD, PERSONAL_DATA_DB_HOST, PERSONAL_DATA_DB_NAME (avec des valeurs par défaut).

mysql-connector-python pour établir la connexion.

Fonction main() (dans filtered_logger.py ou module adéquat) :

Se connecte à la base via get_db()

Extrait tous les utilisateurs

Logue chaque enregistrement en masquant systématiquement les champs name, email, phone, ssn, password, tout en laissant visibles IP, date de dernière connexion et user-agent.

encrypt_password.py

hash_password(password: str) -> bytes : génère un mot de passe salé et hashé avec bcrypt.

is_valid(hashed_password: bytes, password: str) -> bool : vérifie si un mot de passe clair correspond à un hash.

🔧 Contraintes et Bonnes Pratiques
Compatibilité : Python 3.9 sur Ubuntu 20.04 LTS.

Tous les scripts commencent par #!/usr/bin/env python3.

Formatage conforme à pycodestyle v2.5.

Tous les fichiers sont exécutables et se terminent par une newline.

Documentation obligatoire : modules, classes, fonctions (phrases descriptives chacune vérifiées via import).

Fonctions typage annoté.

Longueur du fichier contrôlée avec wc.

✅ Checklist
Tâche	Statut
filter_datum (masquage)	
RedactingFormatter.format	
get_logger + PII_FIELDS	
get_db (connexion sécurisée)	
main() (lecture + masquage + log)	
hash_password + is_valid
