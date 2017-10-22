# coding: utf-8

import os
import markdown
import json
from flask import render_template, request
from flask.blueprints import Blueprint
from app.untils import log, send_success, send_failure
from app.database import note_manager, catalog_manager
from config.constant import static_folder, template_folder

app = Blueprint('article', __name__, static_folder=static_folder, template_folder=template_folder)

@app.route('/')
def page_info():
    return render_template('article2.html')


@app.route('/api/note', methods=['GET'])
def note():
    note_id = request.args.get('note_id', 0)
    rdata = note_manager.note(note_id)
    log('rdata', rdata)
    return send_success(data=rdata)

