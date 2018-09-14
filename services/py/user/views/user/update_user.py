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
from user.bussiness.user_controller import UserController
from base_common.request_service import send_failure, send_success
from config_default.log import debug_log


def clear_fe_data(data):
    """

    :return:
    """
    print(data)
    d = {}
    d['id'] = data.get('id', '')
    d['username'] = data.get('username', '')
    d['password'] = data.get('password', '')
    d['update_time'] = datetime.now()
    return d


def update_user(request):
    """
    更新
    更新一个
    存在就更新，不存在就添加
    1. 判断是否存在
    :param request:
    :return:
    """
    data = clear_fe_data(request)
    user_id = data.get('id', '')
    manger = UserManger()
    ctr = UserController()
    if ctr.exit_user(user_id):
        user_id = manger.update_one_user(data)
    else:
        user_id = manger.add_one_user(data)

    user = manger.get_user(user_id)

    d = {
        'id': user.id,
        'username': user.username,
    }
    return send_success(data=d)
