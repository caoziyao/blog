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

def delete_note(request):
    """
    删除
    存在就更新，不存在就添加
    1. 判断是否存在
    :param request:
    :return:
    """
    ids = request
    manger = NoteManger()

    if isinstance(ids, list):
        manger.delete_mutil_note(ids)
    elif isinstance(ids, dict):
        manger.delete_one_note(ids)
    else:
        # error
        pass

    return 'ok'
