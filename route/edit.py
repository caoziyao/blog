# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint


app = Blueprint('edit', __name__, static_folder='static')


@app.route('/hello')
def edit():
    return render_template('hello.html')