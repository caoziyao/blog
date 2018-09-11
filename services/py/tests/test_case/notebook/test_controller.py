# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
python3 testmain.py notebook
docker exec kuaibiji_srv-pyapp_1 python3 testmain.py notebook
"""
import requests
import json
import unittest
from tests.test_case.base import BaseCase
from notebook.bussiness.notebook_controller import NotebookController


class TestNotebook(BaseCase):

    @unittest.skip('skip')
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

    @unittest.skip('skip')
    def test_update_notebook(self):
        url = self.url_rpc
        headers = self.headers

        d = [
            {'id': 1, 'name': 'aaaaaaaa'},
            {'id': 2, 'name': 'bbbbbb'},
            {'name': 'vvvvv'},
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

        # self.assertEqual(response.status_code, 200)
        print('response', response.content)

    @unittest.skip('skip')
    def test_exit_notebook(self):
        """
        test_exit_notebook
        :return:
        """
        data = [
            {
                'args': {
                    'id': 1,
                },
                'expect': True
            },
            {
                'args': {
                    'id': 0,
                },
                'expect': False
            },
        ]

        ctr = NotebookController()
        for d in data:
            _id = d['args']['id']
            expect = d['expect']
            self.assertEqual(expect, ctr.exit_notebook(_id))

    @unittest.skip('skip')
    def test_delete_notebook(self):
        url = self.url_rpc
        headers = self.headers

        d = [13]

        payload = {
            "service": "srv-notebook",
            "method": "notebook.delete",
            # "request": {'id': 1, 'name': 'abc'},
            "request": d,
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        # self.assertEqual(response.status_code, 200)
        print('response', response.content)
