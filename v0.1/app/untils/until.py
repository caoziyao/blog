# coding: utf-8

import os
import json
import datetime
from .share import ResultCode

def log(*args, **kwargs):

    now = datetime.datetime.now()
    str = now.strftime('%Y-%m-%d %H:%M:%S')
    print('[logger]:', str, '\n', *args, **kwargs)

def load_file(path):
    with open(path, 'r') as f:
        data = f.read()
        s = json.loads(data, encoding='utf-8')
        return s

def send_success(data=''):
    """
    返回 json
    :param data:
    :return:
    """
    return send_json(result_code=ResultCode.success, message='success', data=data)

def send_failure(message, data=''):
    """
    返回 json
    :param data:
    :return:
    """
    return send_json(result_code=ResultCode.failure, message=message, data=data)


def send_json(result_code=ResultCode.success, message='success', data=''):
    """
    返回 json
    :param data:
    :return:
    """
    rdata = {
        'result': result_code.value,
        'message': message,
        'data': data,
    }
    return json.dumps(rdata)

