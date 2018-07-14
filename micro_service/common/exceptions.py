# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/14 
@desc: 异常类
"""


class RPCException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return 'RPCException {}'.format(self.msg)

    __repr__ = __str__


class LogicException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return 'RPCException {}'.format(self.msg)

    __repr__ = __str__


class HTTPException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return 'RPCException {}'.format(self.msg)

    __repr__ = __str__
