# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
from flask_login._compat import unicode

from app import db


class User(db.Document):
    id = db.IntField(required=True)
    user = db.StringField()
    password = db.StringField()
    name = db.StringField()
    email = db.StringField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
