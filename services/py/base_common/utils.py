# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/13 
@desc:
"""


def is_number(num):
    """
    是数字
    :return:
    """
    if (isinstance(num, int)) or (isinstance(num, str) and num.isalnum()):
        return True
    else:
        return False


def toint(num):
    """
    转化数字
    :param num:
    :return:
    """
    try:
        n = int(float(num))
    except Exception as e:
        n = 0

    return n
