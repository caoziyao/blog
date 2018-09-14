# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""
from urllib.parse import quote
from urllib.parse import urlencode


class HTTPClientBase(object):

    def __init__(self, host, port, scheme='http'):
        self.host = host
        self.port = port
        self.scheme = scheme
        self.base_uri = '{}://{}:{}'.format(self.scheme, self.host, self.port)

    def uri(self, path, params=None):
        """
        params = {
            'id': 123,
            'abc': 'un',
        }
        :param path:
        :param params:
        :return:
        """
        path = self.base_uri + quote(path, safe='/:')
        if params:
            p = urlencode(params)
            path = '{}?{}'.format(path, p)

        return path

    def get(self, url, params=None, headers=None):
        raise NotImplementedError

    def post(self, url, params=None, data='', headers=None):
        raise NotImplementedError()

    def delete(self, url, params=None, data='', headers=None):
        raise NotImplementedError

    def put(self, url, params=None, data='', headers=None):
        raise NotImplementedError
