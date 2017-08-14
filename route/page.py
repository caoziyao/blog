# coding: utf-8

import markdown
from flask import  render_template, request
from flask.blueprints import Blueprint
from config.constant import ROOT_DIR, WIKI_ROOT

app = Blueprint('page', __name__, static_folder='static')


def dir_from_url(url):

    dirlist = url.get('f', '').split('_')

    path = '/'.join(dirlist)

    return path

def filename_from_url(url):

    filename = url.get('f', '').split('_')[-1]

    return filename


@app.route('/')
def hello():

    args = request.args
    path = dir_from_url(args)
    filename = filename_from_url(args)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    html = markdown.markdown(content)

    return render_template('page.html', content=html, filename=filename)