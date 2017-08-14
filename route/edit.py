# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint
from server.server import listdir
from config.constant import ROOT_DIR, WIKI_ROOT

app = Blueprint('edit', __name__, static_folder='static')


@app.route('/hello')
def edit():
    folder = 'wiki'
    dirs, files = listdir(folder)

    d = {
        'dirs': dirs,
        'files': files,
    }
    return render_template('edit_hello.html')