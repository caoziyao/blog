# coding: utf-8

import os
import markdown
import json
from flask import render_template, request
from flask.blueprints import Blueprint
from handlers import FileHandler, RenderFileHandler
from config.constant import SEPARATOR
from untils import log
from database import DataManager
from model import note_manager, catalog_manager

app = Blueprint('article', __name__, static_folder='static')


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
def page_info():
    node_id = request.args.get('node_id', 0)
    rdata = note_manager.get_note_content(node_id)
    log('rdata', rdata)
    return render_template('article.html', note=rdata)

