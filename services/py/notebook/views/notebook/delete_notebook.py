# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""

from notebook.database.notebook_manger import NotebookManger
from datetime import datetime


# def clear_fe_data(data):
#     """
#     :return:
#     """
#     if isinstance(data, list):
#         for item in data:
#

def delete_notebook(request):
    """
    更新 notebook
    存在就更新，不存在就添加
    1. 判断是否存在
    :param request:
    :return:
    """
    ids = request
    manger = NotebookManger()

    if isinstance(ids, list):
        manger.delete_mutil_notebook(ids)
    elif isinstance(ids, dict):
        manger.delete_one_notebook(ids)
    else:
        # error
        pass

    return 'ok'
