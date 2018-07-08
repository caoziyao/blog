# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""

import socket


class BaseService(object):

    def __init__(self):
        self.addr = None

        self.set_up()

    def set_up(self):
        self.addr = self.addr_from_socket()

    def addr_from_socket(self):
        """
        :return:
        """
        # 获取本机电脑名
        name = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        addr = socket.gethostbyname(name)

        return addr

    @property
    def metadata(self):
        """
        grpc 返回头
        metadata = [('ip', '127.0.0.1'), ('hello', 'grpc')]
        :return:
        """
        metadata = [
            ('addr', self.addr),

        ]

        return metadata
