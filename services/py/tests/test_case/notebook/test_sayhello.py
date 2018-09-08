# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""
import unittest
from tests.test_case.base import BaseCase

import requests
import json


class TestSayHello(BaseCase):


    @unittest.skip('not')
    def test_get_notebook(self):
        url = self.url_rpc
        headers = self.headers

        payload = {
            "service": "srv-notebook",
            "method": "notebook.get",
            "request": {'id': 1},
            # "params": {"id": 23, "minuend": 42},
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        self.assertEqual(response.status_code, 200)
        print('response', response.content)

    # @unittest.skip('not')
    def test_update_notebook(self):
        url = self.url_rpc
        headers = self.headers

        d = [
            {'id': 1, 'name': 'a'},
            {'id': 1, 'name': 'b'},
            {'id': 1, 'name': 'c'},
        ]

        payload = {
            "service": "srv-notebook",
            "method": "notebook.update",
            # "request": {'id': 1, 'name': 'abc'},
            "request": d,
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        self.assertEqual(response.status_code, 200)
        print('response', response.content)