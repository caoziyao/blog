# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""
import json
from base_common.constants import EnumResponseCode


def send_success(data='', msg='success', code=EnumResponseCode.success.value):
    """

    :param code:
    :param data:
    :param msg:
    :return:
    """
    r = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    return r


def send_failure(data='', msg='failure', code=EnumResponseCode.failure.value):
    """

    :param code:
    :param data:
    :param msg:
    :return:
    """
    r = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    return r
