# coding: utf-8

import os
from flask import  render_template, request
from flask.blueprints import Blueprint
from handlers.file_handler import FileHandler
from config.constant import SEPARATOR
from untils import log

app = Blueprint('folder', __name__, static_folder='static')


def path_from_url(url):
    """
    @Users@cczy@yun@wiki@notebook
    :param url:
    :return: /Users/cczy/yun/wiki/notebook
    """
    sep = 'd'
    if sep in url:
        path = url.get(sep, '').replace(SEPARATOR, '/')
    else:
        return ''

    return path


@app.route('/')
def folder():
    # folder = 'f'
    # args = request.args
    # path = path_from_url(args)
    #
    # log('path', args)
    # f = FileHandler(path)
    #
    # # data = listdir(path)
    # data = f.all_files()

    return render_template('index.html', current_dir='', parent_dir='', dirs_files='')