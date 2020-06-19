import datetime
import json

from flask import request, jsonify
from werkzeug.exceptions import HTTPException, BadRequest

from app.routers.api import api
from arcgis.geocoding import Geocoder, get_geocoders, geocode, reverse_geocode
from app.models.padawan_model import Location, AssemblyPoint


# Cluster Level API
@api.route('/backend/cluster/find', methods=['GET'])
def find_all_cluster():
    all_cluster = AssemblyPoint.objects.all()
    return jsonify(all_cluster)


@api.route('/backend/cluster/find/<cluster_name>', methods=['GET'])
def find_cluster(cluster_name):
    cluster = AssemblyPoint.objects(cluster_name=cluster_name).first()
    return jsonify(cluster)


@api.route('/backend/cluster/create', methods=['POST'])
def create_cluster():
    data = request.json
    cluster_name = data['cluster_name']
    date = datetime.datetime.now()
    cluster = AssemblyPoint(cluster_name=cluster_name, created_date=date, updated_date=date)
    cluster.save()
    return jsonify({'cluster name': cluster_name, 'result': True, 'description': 'Create new cluster success'})


@api.route('/backend/cluster/delete/<name>', methods=['DELETE'])
def delete_cluster(name):
    AssemblyPoint.objects(cluster_name=name).delete()
    Location.objects(cluster_name=name).delete()
    return jsonify({'cluster name': name, 'result': True, 'description': 'Delete cluster success'})


@api.route('/backend/cluster/calculate/middle-point', methods=['POST'])
def calculate_middle_point():
    data = request.json
    cluster_name = data['cluster_name']

    location_list = Location.objects(cluster_name=cluster_name).all()
    if len(location_list) == 0:
        exception = BadRequest()
        exception.description = 'No Location Exist In This Cluster'
        raise exception

    return jsonify(location_list)


@api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response