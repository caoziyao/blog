# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
import json
import functools
from enum import Enum
from .constants import ResultCode
from datetime import datetime
from datetime import date
from database import redis_client


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def unauthorized():
    # abort(401)
    return send_failure(msg='please login in')


def login_required(func):
    """
    登陆装饰器，func的执行必须是已登陆用户，否则跳转到登陆页面
    :param func: 被装饰的函数
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # user_info = get_user_info(self.token_cache_id)
        token = 'jwmi hello ranndeeerom id'
        user_info = redis_client.get_bylock(token)
        if user_info is None:
            return unauthorized()
            # raise HTTPError(401)
        # elif user_info and toint(user_info.get('member_id', 0)) <= 0:
        #     raise HTTPError(401)
        # 将用户信息赋给view类
        # self.user_info = user_info
        return func(*args, **kwargs)

    return wrapper


def send_success(data='', msg='success', code=ResultCode.success):
    """
    :return:
    """
    return send_json(data=data, msg=msg, code=code)


def send_failure(data='', msg='failure', code=ResultCode.failure):
    """
    :return:
    """
    # errmsg = msg or error_msg_from_code(code)
    return send_json(data=data, msg=msg, code=code)


def send_json(data, msg, code=ResultCode.success):
    """
    :return:
    """
    if isinstance(code, Enum):
        code = code.value

    result_dict = {
        'code': code,
        'msg': msg,
        'data': data
    }
    return json.dumps(result_dict, cls=ComplexEncoder)
