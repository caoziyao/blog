# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/15 
@desc:
"""
from database import codes
from utilities.utils import is_identifier


def get_error_msg(request_data):
    """

    :param request_data:
    :return:
    """
    code = request_data.get('code', '')
    if is_identifier(code):
        code = int(code)
        msg = error_msg_from_code(code)
    else:
        msg = 'not found message'

    return msg

def error_msg_from_code(code):
    """
    获得错误信息
    :param code: int
    :return:
    """
    d = codes
    msg = d.get(code, 'not found message')

    return msg


