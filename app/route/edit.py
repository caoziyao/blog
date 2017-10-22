# coding: utf-8

import json
import os
from flask import render_template, request
from flask.blueprints import Blueprint
from app.handlers import FileHandler, RenderFileHandler
from app.untils import log, send_success, send_failure
from app.handlers import config
from app.database import DBManager, note_manager, catalog_manager
from config.constant import static_folder, template_folder

app = Blueprint('edit', __name__, static_folder=static_folder, template_folder=template_folder)


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
    return render_template('edit2.html')


@app.route('/new')
def edit_new():
    return render_template('edit_new.html')


@app.route('/api/catalog', methods=['GET'])
def edit_load_catalog():

    column = catalog_manager.catalog()
    return send_success(data=column)


def save_page(data):
    db = DBManager()
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
        result, note_id = note_manager.new_note(data=data)
        # db.insert('tb_note', data=data)
    else:
        result = note_manager.update_note(note_id, data=data)
        # db.update('tb_note', data=data, condition=cond)

    return result, note_id


@app.route('/api/edit_page', methods=['POST'])
def edit_page():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    result, note_id = save_page(data)
    if result:
        r = {
            'note_id': note_id
        }
        return send_success(data=r)
    else:
        return send_failure(message='保存失败')
    # rdata = {
    #     'status': 1,
    #     'data': '',
    #     'msg': '',
    # }
    # return json.dumps(rdata)
