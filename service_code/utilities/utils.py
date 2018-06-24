# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/15 
@desc:
"""


def is_identifier(identifier):
    # 校验是数字，数字字符串
    if (isinstance(identifier, str) and identifier.isdigit()) or isinstance(identifier, int):
        return True
    else:
        return False
