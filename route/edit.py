# coding: utf-8

import json
import os
from flask import render_template, request
from flask.blueprints import Blueprint
from handlers import FileHandler, RenderFileHandler
from untils import log
from handlers import config
from database import DataManager
from model import note_manager, catalog_manager

app = Blueprint('edit', __name__, static_folder='static')


def test_file():
    root_path = config.root_path

    f = FileHandler(root_path)

    parent_path = f.current_path()
    current_path = f.current_path()

    data = f.all_files()

    d = {
        'parent': parent_path,
        'current': current_path,
    }

    data.update(d)

    return data


@app.route('/')
def edit():

    rdata = []
    catalogs = catalog_manager.load_columns()
    for cat in catalogs:
        cat_id = cat['id']
        notes = note_manager.get_notes(cat_id)
        d = {
            'catalog_id': cat_id,
            'title': cat['title'],
            'notes': notes,
        }
        rdata.append(d)

    # log('members', catalogs)
    # log('notes', notes)

    return render_template('edit.html', rdata=rdata)


@app.route('/api/load_catalog', methods=['POST'])
def edit_load_catalog():

    data = request.data.decode('utf-8')
    data = json.loads(data)

    catalog_id = data.get('catalog_id', '')

    column = note_manager.get_catalog(catalog_id)
    rdata = {
        'status': 1,
        'data': column,
        'msg': '',
    }

    return json.dumps(rdata)

@app.route('/api/load_note', methods=['POST'])
def edit_load_note():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    catalog_id = data.get('catalog_id', '')
    note_id = data.get('note_id', '')

    column = note_manager.get_note_content(note_id)
    if column:
        rdata = {
            'status': 1,
            'data': column[0],
            'msg': '',
        }
    else:
        rdata = {
            'status': 1,
            'data': {},
            'msg': '',
        }

    return json.dumps(rdata)