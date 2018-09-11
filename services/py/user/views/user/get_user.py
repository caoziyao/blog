# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""
from user.bussiness.user_controller import UserController


def get_user(request):
    """
    get
    :param request:
    :return:
    """
    _id = request['id']

    ctr = UserController()
    # manger = NotebookManger()
    data = ctr.get_user(_id)
    return data
