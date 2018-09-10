# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""
from notebook.bussiness.note_controller import NoteController


def get_note(request):
    """
    get notebook
    :param request:
    :return:
    """
    _id = request['id']

    ctr = NoteController()
    # manger = NotebookManger()
    data = ctr.get_note(_id)
    return data
