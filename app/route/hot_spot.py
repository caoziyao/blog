# coding: utf-8

import json
import os
from flask import render_template, request
from flask.blueprints import Blueprint
from app.untils import log
from app.database import DataManager, DataCache
from app.model import note_manager, catalog_manager
from config.constant import static_folder, template_folder

app = Blueprint('hot_spot', __name__, static_folder=static_folder, template_folder=template_folder)


def init_click_num(note_id):
    """
    初始点击数
    :return:
    """
    r = DataCache().redis
    key = 'visit:{}:totals'.format(str(note_id))
    if not r.exists(key):
        r.set(key, 65536)
    return r.get(key).decode('utf-8')


def incr_click_num(note_id):
    """
    点击数
    :return:
    """
    r = DataCache().redis
    key = 'visit:{}:totals'.format(str(note_id))
    r.incr(key)
    return r.get(key).decode('utf-8')


@app.route('/incr_click_number', methods=['POST'])
def incr_click_number():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    note_id = data.get('note_id', 0)
    n = incr_click_num(note_id)

    rdata = {
        'number': n,
    }
    log('number', rdata)

    return json.dumps(rdata)
