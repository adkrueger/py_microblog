from flask import render_template
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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
