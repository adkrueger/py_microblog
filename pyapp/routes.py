from flask import render_template, flash, redirect, url_for
from pyapp import app
from pyapp.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aaron'}
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
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
