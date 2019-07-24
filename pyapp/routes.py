from flask import render_template
from pyapp import app


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
