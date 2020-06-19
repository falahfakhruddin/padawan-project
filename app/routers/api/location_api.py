import json

from flask import request, jsonify
from werkzeug.exceptions import HTTPException

from app.routers.api import api
from arcgis.geocoding import Geocoder, get_geocoders, geocode, reverse_geocode
from app.models.padawan_model import Location


# Location level API
@api.route('/backend/available-location/search/<area>', methods=['GET'])
def search_available_location(area):

    print(area)
    print(type(area))
    g1 = geocode(area)
    geocode_collection = [{} for i in range(0, len(g1))]
    for i in range(0, len(g1)):
        geocode_collection[i]['address'] = g1[i]['address']
        geocode_collection[i]['location'] = g1[i]['location']

    return jsonify(geocode_collection)


@api.route('/backend/location/find/<cluster>', methods=['GET'])
def find_location(cluster):
    location = Location.objects(cluster_name=cluster).all()
    return jsonify(location)


@api.route('/backend/location/save', methods=['POST'])
def save_location():
    data = request.json
    address = data['address']
    location = data['location']
    name = data['name']
    cluster_name = data['cluster_name']
    location = Location(name=name, cluster_name=cluster_name, address=address, location=location)
    location.save()
    return jsonify(data)


@api.route('/backend/location/delete/<cluster>/<name>', methods=['DELETE'])
def delete_location(cluster, name):
    Location.objects(name=name, cluster_name=cluster).delete()
    return jsonify({'name': name, 'result': True})


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
