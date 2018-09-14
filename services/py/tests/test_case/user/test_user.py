# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/11 
@desc:
docker exec prj-kuaibiji_srv-user_1 python3 testmain.py user
"""
import requests
import json
import unittest
from tests.test_case.base import BaseCase
from user.bussiness.user_controller import UserController


class TestUser(BaseCase):

    @unittest.skip('skip')
    def test_get_user(self):
        url = self.url_rpc
        headers = self.headers

        payload = {
            "service": "srv-user",
            "method": "user.get",
            "request": {'id': 2},
            # "params": {"id": 23, "minuend": 42},
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        print('response', response.content)
        self.assertEqual(response.status_code, 200)

    # @unittest.skip('skip')
    def test_update_user(self):
        url = self.url_rpc
        headers = self.headers

        d = {'username': 'bbbb'}

        payload = {
            "service": "srv-user",
            "method": "user.update",
            # "request": {'id': 1, 'name': 'abc'},
            "request": d,
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        print('response', response.content)
        self.assertEqual(response.status_code, 200)

    @unittest.skip('skip')
    def test_exit_user(self):
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

        ctr = UserController()
        for d in data:
            _id = d['args']['id']
            expect = d['expect']
            self.assertEqual(expect, ctr.exit_user(_id))

    @unittest.skip('skip')
    def test_delete_user(self):
        url = self.url_rpc
        headers = self.headers

        d = {
            'id': 1
        }

        payload = {
            "service": "srv-user",
            "method": "user.delete",
            "request": d,
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        #
        print('response', response.content)
        self.assertEqual(response.status_code, 200)