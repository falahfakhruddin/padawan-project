from flask import Blueprint

api = Blueprint('api', __name__)

from . import location_api, user_cluster_api