# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint


app = Blueprint('page', __name__, static_folder='static')


@app.route('/<filename>')
def hello(filename):
    return render_template('hello.html')