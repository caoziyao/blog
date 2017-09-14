# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint

app = Blueprint('edit', __name__, static_folder='static')


@app.route('/')
def edit():

    return render_template('edit_hello.html')