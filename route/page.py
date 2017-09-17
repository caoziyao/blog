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

    return render_template('page.html', sourceContent=source, filePath=path, markDownContent=html, filename=filename, file_type=file_type)


def save_page(path, content):
    # log('path', path, content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def save_page_to_db(path, content):
    db = DataManager()

    data = {
        'title': path,
        'content': content
    }

    cond = {
        'title': path,
    }
    res = db.fetch_rows('tb_note', condition=cond, fetchone=True)
    if not res:

        db.insert('tb_note', data=data)
    else:
        cond = {
            'id': res.get('id', 0),
            'title': path,
        }
        db.update('tb_note', data=data, condition=cond)
        print('res', res)


@app.route('/api/edit_page', methods=['POST'])
def edit_page():
    # data = request.form.get('data', '')
    data = request.data.decode('utf-8')
    data = json.loads(data)

    content = data.get('content', '')
    path = data.get('path', '')

    # save_page(path, content)
    save_page_to_db(path, content)


    rdata = {
        'status': 1,
        'data': '',
        'msg': '',
    }
    return json.dumps(rdata)