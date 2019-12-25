from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Juan'},
            'body': 'Lovin\' me some tasty boigas!'
        },
        {
            'author': {'username': 'Barbara'},
            'body': 'I\'m vegan and I hate boigas!'
        }
    ]
    return render_template('index.html', title="Home Page", posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        curr_user = User.query.filter_by(username=form.username.data).first()
        if curr_user is None or not curr_user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(curr_user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        curr_user = User(username=form.username.data, email=form.email.data)
        curr_user.set_password(form.password.data)
        db.session.add(curr_user)
        db.session.commit()
        flash('Congrats! You\'re now registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    curr_user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': curr_user, 'body': 'Test post #1 boiiii'},
        {'author': curr_user, 'body': 'Test post #2 feller'}
    ]
    return render_template('user.html', user=curr_user, posts=posts)
