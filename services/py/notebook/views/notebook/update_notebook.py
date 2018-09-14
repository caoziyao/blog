# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/9 
@desc:
"""
from notebook.bussiness.notebook_controller import NotebookController
from notebook.database.notebook_manger import NotebookManger
from datetime import datetime
from base_common.request_service import send_failure, send_success


def clear_data(data):
    """
    :return:
    """
    d = {}
    d['id'] = data.get('id', '')
    d['name'] = data.get('name', '')
    d['update_time'] = datetime.now()
    return d


def update_notebook(request):
    """
    更新 notebook
    存在就更新，不存在就添加
    1. 判断是否存在
    :param request:
    :return:
    """
    data = clear_data(request)

    ctr = NotebookController()
    manger = NotebookManger()

    _id = data.get('id', '')
    if ctr.exit_notebook(_id):
        _id = manger.update_one_notebook(data)
    else:
        _id = manger.add_one_notebook(data)

    notebook = ctr.get_notebook(_id)
    return send_success(data=notebook)
