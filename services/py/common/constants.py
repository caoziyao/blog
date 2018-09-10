# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""
from enum import Enum, unique

@unique
class EnumResponseCode(Enum):
    """
    错误码
    """
    success = '0'
    failure = '0100110'