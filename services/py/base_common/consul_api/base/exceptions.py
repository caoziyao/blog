# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""


class ConsulException(Exception):
    pass


class NotFound(ConsulException):
    pass


class Timeout(ConsulException):
    pass


class BadRequest(ConsulException):
    pass
