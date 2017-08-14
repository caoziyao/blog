# coding: utf-8

import os
from flask import  render_template, request
from flask.blueprints import Blueprint
from server.server import listdir
from config.constant import ROOT_DIR, WIKI_ROOT
app = Blueprint('folder', __name__, static_folder='static')


def dir_from_url(url):

    root = ROOT_DIR
    dirlist = url.get('d', '').split('_')

    path = '/'.join(dirlist)

    return path


@app.route('/')
def hello():
    # folder = 'f'
    args = request.args
    path = dir_from_url(args)

    data = listdir(path)

    return render_template('index.html', dirs_files=data)