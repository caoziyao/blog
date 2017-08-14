# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint


app = Blueprint('index', __name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')