# coding: utf-8

from flask import  render_template
from flask.blueprints import Blueprint
from server.server import listdir
from config.constant import ROOT_DIR, WIKI_ROOT

app = Blueprint('index', __name__, static_folder='static')


@app.route('/')
def index():
    folder = WIKI_ROOT
    data = listdir(folder)

    return render_template('index.html', dirs_files=data)