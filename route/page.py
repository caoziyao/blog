# coding: utf-8

import os
import markdown
from flask import render_template, request
from flask.blueprints import Blueprint
from handlers import FileHandler, RenderFileHandler
from config.constant import SEPARATOR
from untils import log

app = Blueprint('page', __name__, static_folder='static')


def path_from_url(url):

    sep = 'f'
    if sep in url:
        path = url.get('f', '').replace(SEPARATOR, '/')
    else:
        path = ''
    return path

def filename_from_url(url):

    filename = url.get('f', '').split(SEPARATOR)[-1]
    return filename


@app.route('/')
def hello():

    args = request.args
    path = path_from_url(args)
    filename = filename_from_url(args)

    render = RenderFileHandler(path)
    extent = render.file_extension()
    html = render.render_file()
    source = render.content_from_file()

    file_type = extent[1:]

    return render_template('page.html', sourceContent=source, markDownContent=html, filename=filename, file_type=file_type)