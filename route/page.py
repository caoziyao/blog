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

app = Blueprint('page', __name__, static_folder='static')


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
    args = request.args
    path = path_from_url(args)
    filename = filename_from_url(args)

    render = RenderFileHandler(path)
    extent = render.file_extension()
    html = render.render_file()
    source = render.content_from_file()

    file_type = extent[1:]

    return render_template('page.html', sourceContent=source, filePath=path, markDownContent=html, filename=filename,
                           file_type=file_type)


def save_file(path, content):
    # log('path', path, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


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
