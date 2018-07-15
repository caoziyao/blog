# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/14 
@desc:
"""
from flask import request


class BaseHandler(object):

    def __init__(self):
        self.token = ''
        self.user_agent = ''
        self.debug = False
        self.set_up()

    def set_up(self):
        self.token = request.headers.get('Token', '').lower()
        self.user_agent = request.headers.get('User-Agent', '').lower()
        self.debug = request.headers.get('debug', '').lower()
