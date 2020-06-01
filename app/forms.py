# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask_wtf import Form
from wtforms import StringField, TextAreaField, DateTimeField, PasswordField


class ExampleForm(Form):
    title = StringField(u'Title')
    content = TextAreaField(u'Content')
    date = DateTimeField(u'Date', format='%d/%m/%Y %H:%M')
# recaptcha = RecaptchaField(u'Recaptcha')


class LoginForm(Form):
    user = StringField(u'User')
    password = PasswordField(u'Password')
