# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""

import requests
import json
import unittest
from tests.test_case.base import BaseCase
from user.bussiness.user_controller import UserController
from base_common.consul_api.std.http_client import HTTPClient

class TestHttpClient(BaseCase):

    # @unittest.skip('skip')
    def test_httpclient(self):

        c = HTTPClient('127.0.0.1', 4001)
        path = '/du'
        params = {
            'id': 1,
        }
        r = c.get(path, params)

        print(r)
        print(r.body)
        self.assertEqual(r.code, 200)
