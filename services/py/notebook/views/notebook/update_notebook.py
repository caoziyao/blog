# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/9 
@desc:
"""
from notebook.database.notebook_manger import NotebookManger


def update_notebook(request):
    """
    更新 notebook
    :param request:
    :return:
    """
    data = request

    manger = NotebookManger()
    manger.add_notebook(data)

    return data

