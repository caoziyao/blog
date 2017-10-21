# coding: utf-8

import os
import markdown
import json
from flask import render_template, request
from flask.blueprints import Blueprint
from app.untils import log
from app.database import note_manager, catalog_manager
from config.constant import static_folder, template_folder

app = Blueprint('article', __name__, static_folder=static_folder, template_folder=template_folder)

@app.route('/')
def page_info():
    node_id = request.args.get('node_id', 0)
    rdata = note_manager.get_note_content(node_id)
    log('rdata', rdata)
    return render_template('article.html', note=rdata)

