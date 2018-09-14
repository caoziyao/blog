# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8
@desc:
python3 testmain.py notebook
docker exec prj-kuaibiji_srv-pyapp_1 python3 testmain.py note
"""
import requests
import json
import unittest
from tests.test_case.base import BaseCase
from notebook.bussiness.note_controller import NoteController


class TestNote(BaseCase):

    @unittest.skip('not')
    def test_get_note(self):
        url = self.url_rpc
        headers = self.headers

        payload = {
            "service": "srv-notebook",
            "method": "note.get",
            "request": {'id': 1},
            # "params": {"id": 23, "minuend": 42},
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        self.assertEqual(response.status_code, 200)
        print('response', response.content)

    # @unittest.skip('not')
    def test_update_note(self):
        url = self.url_rpc
        headers = self.headers

        d = {'id': 11, 'name': 'aaaaa', 'notebook_id': 16}

        payload = {
            "service": "srv-notebook",
            "method": "note.update",
            # "request": {'id': 1, 'name': 'abc'},
            "request": d,
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        # self.assertEqual(response.status_code, 200)
        print('response', response.content)

    @unittest.skip('test_exit_note')
    def test_exit_note(self):
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

        ctr = NoteController()
        for d in data:
            _id = d['args']['id']
            expect = d['expect']
            self.assertEqual(expect, ctr.exit_note(_id))

    @unittest.skip('not')
    def test_delete_notebook(self):
        url = self.url_rpc
        headers = self.headers

        d = [13]

        payload = {
            "service": "srv-notebook",
            "method": "note.delete",
            # "request": {'id': 1, 'name': 'abc'},
            "request": d,
            "jsonrpc": "2.0",
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers)

        # self.assertEqual(response.status_code, 200)
        print('response', response.content)
