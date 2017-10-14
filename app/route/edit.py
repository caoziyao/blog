# coding: utf-8

import json
import os
from flask import render_template, request
from flask.blueprints import Blueprint
from app.handlers import FileHandler, RenderFileHandler
from app.untils import log
from app.handlers import config
from app.database import DataManager
from app.model import note_manager, catalog_manager
from config.constant import static_folder, template_folder

app = Blueprint('edit', __name__, static_folder=static_folder, template_folder=template_folder)

# print('aaaaa', static_folder, template_folder)

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
    note_id = request.args.get('node_id', 1)

    rdata = []
    catalogs = catalog_manager.load_columns()
    column = note_manager.get_note_content(note_id)

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

    return render_template('edit.html', rdata=rdata, column=column)


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



def save_page(data):
    db = DataManager()

    note_id = data.get('note_id', 0)
    content = data.get('content', '')
    title = data.get('title', '')
    catalog_id = data.get('catalog_id')

    data = {
        'title': title,
        'content': content,
        'catalog_id': catalog_id,
    }

    cond = {
        'id': note_id,
    }
    res = db.fetch_rows('tb_note', condition=cond, fetchone=True)
    if not res:
        db.insert('tb_note', data=data)
    else:
        db.update('tb_note', data=data, condition=cond)


@app.route('/api/edit_page', methods=['POST'])
def edit_page():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    save_page(data)

    rdata = {
        'status': 1,
        'data': '',
        'msg': '',
    }
    return json.dumps(rdata)
