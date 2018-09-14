# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""
import requests
from collections import namedtuple
from base_common.consul_api.base.http_client import HTTPClientBase
from base_common.consul_api.base.exceptions import BadRequest, ConsulException, NotFound

# from base_common.consul_api.base.cb import CB

Response = namedtuple('Response', ['code', 'headers', 'body'])


def callback(fn):
    """
    fn: get post delete put
    :return:
    """

    def wrap(self, *args, **kwargs):
        res = fn(self, *args, **kwargs)
        r = self.response(res)
        self._status(r)
        return r

    return wrap


class HTTPClient(HTTPClientBase):

    def __init__(self, *args, **kwargs):
        super(HTTPClient, self).__init__(*args, **kwargs)
        self.session = requests.session()
        # self.callback = CB

    def _status(self, response, allow_404=True):
        """
        response： namedtuple
        :return:
        """
        code = response.code
        if code == 404:
            raise NotFound('not found')

    def response(self, response):
        """
        response: requests 返回值
        :return:
        """
        d = {
            'code': response.status_code,
            'headers': response.headers,
            'body': response.text,
        }
        return Response(**d)

    @callback
    def get(self, path, params=None, headers=None):
        """

        :param url:
        :return:
        """
        uri = self.uri(path, params)
        print('uri', uri)
        r = self.session.get(uri, headers=headers)
        return r

    @callback
    def post(self, path, params=None, data='', headers=None):
        """
        :return:
        """
        uri = self.uri(path, params)
        r = self.session.post(uri, data=data, headers=headers)
        return r

    @callback
    def delete(self, path, params=None, data='', headers=None):
        """
        :return:
        """
        uri = self.uri(path, params)
        r = self.session.delete(uri, data=data, headers=headers)
        return r

    @callback
    def put(self, path, params=None, data='', headers=None):
        """
        :return:
        """
        uri = self.uri(path, params)
        r = self.session.put(uri, data=data, headers=headers)
        return r
