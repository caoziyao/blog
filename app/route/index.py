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

app = Blueprint('index', __name__, static_folder=static_folder, template_folder=template_folder)


@app.route('/test')
def test():
    return render_template('test.html')


def counter_page(total):
    """
    计算总页数
    :param total: 总数目
    :return:
    """
    pre_page = 20

    div = divmod(total, pre_page)
    i = div[0]
    m = div[1]
    total_page = i if m == 0 else i + 1

    return total_page


@app.route('/page', methods=['POST'])
def page():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    page_no = data.get('page_no', 0)
    notes = note_manager.all_notes(page_no)

    for n in notes:
        n['update_time'] = str(n['update_time'])

    rdata = {
        'notes': notes,
    }
    log('members', rdata)

    return json.dumps(rdata)

@app.route('/catalog', methods=['POST'])
def catalog():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    catalog_id = data.get('catalog_id', 0)
    notes = note_manager.get_notes(catalog_id)

    for n in notes:
        n['update_time'] = str(n['update_time'])

    rdata = {
        'notes': notes,
    }
    log('members', rdata)

    return json.dumps(rdata)

@app.route('/')
def index():
    # 页数
    page_no = request.args.get('page', 1)


    catalogs = catalog_manager.load_columns()
    notes = note_manager.all_notes(page_no)
    total = note_manager.total_page()

    total_page = counter_page(total)

    rdata = {
        'catalogs': catalogs,
        'notes': notes,
        'total_page': total_page,
    }
    log('members', catalogs)

    return render_template('index.html', rdata=rdata)


@app.route('/api/load_catalog', methods=['POST'])
def load_catalog():
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
def load_note():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    catalog_id = data.get('catalog_id', '')
    note_id = data.get('note_id', '')

    column = note_manager.get_note_content(note_id)
    if column:
        rdata = {
            'status': 1,
            'data': column,
            'msg': '',
        }
    else:
        rdata = {
            'status': 1,
            'data': {},
            'msg': '',
        }

    return json.dumps(rdata)
