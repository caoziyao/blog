# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/9 
@desc:
"""
from notebook.database.notebook_manger import NotebookManger
from datetime import datetime


def clear_data(data):
    """

    :return:
    """
    d = {}
    d['id'] = data.get('id', '')
    d['name'] = data.get('name', '')
    d['update_time'] = datetime.now()
    return d


def clear_fe_data(data):
    """

    :return:
    """
    if isinstance(data, list):
        l = []
        for item in data:
            d = clear_data(item)
            l.append(d)
        return l
    elif isinstance(data, dict):
        data = clear_data(data)
        return data
    else:
        # error
        return {}


def update_notebook(request):
    """
    更新 notebook
    存在就更新，不存在就添加
    1. 判断是否存在
    :param request:
    :return:
    """
    data = clear_fe_data(request)
    manger = NotebookManger()

    if isinstance(data, list):
        manger.add_mutil_notebook(data)
    elif isinstance(data, dict):
        manger.add_one_notebook(data)
    else:
        # error
        pass

    return 'ok'
