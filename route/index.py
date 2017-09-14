# coding: utf-8

import json
import os
from flask import  render_template
from flask.blueprints import Blueprint
from handlers.file_handler import  FileHandler
from untils import read_config, log

app = Blueprint('index', __name__, static_folder='static')



@app.route('/')
def index():
    config = read_config()
    root_path = config.get('root_path', '')


    f = FileHandler(root_path)

    parent_path = f.parent_path(root_path)
    current_path = f.current_path()

    data = f.all_files()

    d = {
        'parent': parent_path,
        'current': current_path,
    }

    data.update(d)

    return render_template('index.html', dirs_files=data)