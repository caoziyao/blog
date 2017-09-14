# coding: utf-8

import json
import os
from flask import  render_template
from flask.blueprints import Blueprint
from handlers.file_handler import listdir
from untils import read_config

app = Blueprint('index', __name__, static_folder='static')



@app.route('/')
def index():

    config = read_config()

    root_path = config.get('root_path', '')

    data = listdir(root_path)

    d = {
        'parent': root_path.replace('/', '_'),
        'current': root_path.replace('/', '_'),
    }

    data.update(d)

    return render_template('index.html', dirs_files=data)