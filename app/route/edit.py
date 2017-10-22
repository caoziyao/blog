# coding: utf-8

import json
import os
from flask import render_template, request
from flask.blueprints import Blueprint
from app.untils import log, send_success, send_failure
from app.database import DBManager, note_manager, catalog_manager
from config.constant import static_folder, template_folder

app = Blueprint('edit', __name__, static_folder=static_folder, template_folder=template_folder)


@app.route('/')
def edit():
    """
    编辑入口
    :return:
    """
    return render_template('edit2.html')


@app.route('/new')
def edit_new():
    """
    新建
    :return:
    """
    return render_template('edit_new.html')


@app.route('/api/catalog', methods=['GET'])
def edit_load_catalog():
    """
    加载目录
    :return:
    """
    column = catalog_manager.catalog()
    return send_success(data=column)


def save_page(data):
    """
    保存页面
    :param data:
    :return:
    """
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
    else:
        result = note_manager.update_note(note_id, data=data)

    return result, note_id


@app.route('/api/edit_page', methods=['POST'])
def edit_page():
    """
    编辑页面
    :return:
    """
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
