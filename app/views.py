# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm
from .forms import ExampleForm, LoginForm
from .models import User


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new/')
@login_required
def new():
    form = ExampleForm()
    return render_template('new.html', form=form)


@app.route('/save/', methods=['GET', 'POST'])
@login_required
def save():
    form = ExampleForm()
    if form.validate_on_submit():
        print("saving the data:")
        print(form.title.data)
        print(form.content.data)
        print(form.date.data)
        flash('data saved!')
    return render_template('new.html', form=form)



# === User login methods ===

@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    print(g.user)
    print(g.user.is_authenticated)
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(g.user)

    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/selasarakademik')
def selmik():
    return redirect('https://drive.google.com/drive/u/1/folders/1cf4gHA0sTp_Q7alG-b3fQs0N6-OQTi6P')


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))

# ====================
