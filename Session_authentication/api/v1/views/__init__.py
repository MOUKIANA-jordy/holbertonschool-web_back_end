#!/usr/bin/env python3
"""Initialize views blueprint"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# importer les routes APRÈS la création du blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *
