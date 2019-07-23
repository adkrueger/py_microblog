from flask import Flask

app = Flask(__name__)

from pyapp import routes
