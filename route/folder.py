# coding: utf-8

import os
from flask import  render_template
from flask.blueprints import Blueprint
from server.server import listdir

app = Blueprint('folder', __name__, static_folder='static')


@app.route('/<folder>')
def hello(folder):
    # folder = 'f'

    path = os.path.join('wiki', folder)
    data = listdir(path)

    return render_template('index.html', dirs_files=data)