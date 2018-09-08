# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""
from notebook.database.notebook_manger import NotebookManger


def get_notebook(request):
    """
    get notebook
    :param request:
    :return:
    """
    print('parms', request)
    _id = request['id']

    manger = NotebookManger()
    data = manger.get_notebook(_id)
    return data
