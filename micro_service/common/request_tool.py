# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
import json
from enum import Enum
from .constant import ResultCode
from datetime import datetime
from datetime import date


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


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
