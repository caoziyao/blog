# coding: utf-8

import os
from flask import  render_template, request
from flask.blueprints import Blueprint
from handlers.file_handler import listdir

app = Blueprint('folder', __name__, static_folder='static')


def dir_from_url(url):

    dirlist = url.get('d', '').split('_')
    path = '/'.join(dirlist)

    return path


@app.route('/')
def folder():
    # folder = 'f'
    args = request.args
    path = dir_from_url(args)

    data = listdir(path)

    return render_template('index.html', current_dir=path, parent_dir = path, dirs_files=data)