# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""
from notebook.database.note_manger import NoteManger
from datetime import datetime
from notebook.bussiness.notebook_controller import NotebookController
from notebook.bussiness.note_controller import NoteController
from base_common.request_service import send_failure, send_success
from config_default.log import debug_log


def clear_fe_data(data):
    """

    :return:
    """
    print(data)
    d = {}
    d['id'] = data.get('id', '')
    d['name'] = data.get('name', '')
    d['notebook_id'] = data.get('notebook_id', '')
    d['update_time'] = datetime.now()
    return d


def update_note(request):
    """
    更新 notebook
    更新一个 notebook
    存在就更新，不存在就添加
    1. 判断是否存在
    :param request:
    :return:
    """

    nbctr = NotebookController()
    n = NoteController()
    data = clear_fe_data(request)

    debug_log.info(data)
    notebook_id = data.get('notebook_id', '')
    note_id = data.get('id', '')
    manger = NoteManger()

    if nbctr.exit_notebook(notebook_id):

        if n.exit_note(note_id):
            last_id = manger.update_one_note(data)
        else:
            last_id = manger.add_one_note(data)

        if last_id:
            data = manger.get_note(last_id)
            d = {
                'id': data.id,
                'name': data.name,
                'content': data.content,
            }
            return send_success(data=d)
        else:
            return send_failure(msg='add note failure')
    else:
        return send_failure(msg='notebook not exit')
