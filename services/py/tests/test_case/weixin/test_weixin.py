# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/13
@desc:
docker exec prj-kuaibiji_srv-weixin_1 python3 testmain.py weixin
"""
import requests
import json
import unittest
from tests.test_case.base import BaseCase


class TestWeixin(BaseCase):

    # @unittest.skip('skip')
    def test_get_weixin(self):
        url = self.url_rpc
        headers = self.headers

        payload = {
            "service": "srv-weixin",
            "method": "weixin.get",
            "request": {'id': 2},
            # "params": {"id": 23, "minuend": 42},
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        print('response', response.content)
        self.assertEqual(response.status_code, 200)

