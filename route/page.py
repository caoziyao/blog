# coding: utf-8

import markdown
from flask import  render_template, request
from flask.blueprints import Blueprint
from handlers.file_handler import FileHandler
from config.constant import SEPARATOR

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

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    html = markdown.markdown(content)

    return render_template('page.html', content=html, filename=filename)