from app import db

import datetime


class Location(db.Document):

    name = db.StringField(max_length=120, required=True, unique=True)

    cluster_name = db.StringField(max_length=120, required=True)

    address = db.StringField(max_length=123, required=True)

    location = db.DictField(required=True)


class AssemblyPoint(db.Document):

    cluster_name = db.StringField(max_length=120, required=True, unique=True)

    middle_point = db.DictField()

    created_date = db.DateTimeField(default=datetime.datetime.now())

    updated_date = db.DateTimeField()