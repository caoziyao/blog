# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""
from user.database.user_manger import UserManger
from datetime import datetime


def delete_user(request):
    """
    删除
    存在就更新，不存在就添加
    1. 判断是否存在
    :param request:
    :return:
    """
    _id = request['id']
    manger = UserManger()

    manger.delete_one_user(_id)

    return 'ok'
