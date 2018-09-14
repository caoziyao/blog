# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/13 
@desc:
docker exec prj-kuaibiji_srv-notebook_1 python3 testmain.py utils
"""
import requests
import json
import unittest
from tests.test_case.base import BaseCase
from base_common.utils import is_number, toint


class TestNotebook(BaseCase):

    @unittest.skip('skip')
    def test_isnumber(self):

        data = [
            {
                'args': 1,
                'expect': True,
            },
            {
                'args': '21',
                'expect': True,
            },
            {
                'args': '',
                'expect': False,
            },
            {
                'args': '12.212',
                'expect': False,
            },
            {
                'args': 3232.111,
                'expect': False,
            },

        ]

        for each in data:
            args = each.get('args', '')
            expect = each.get('expect', '')

            self.assertEqual(expect, is_number(args))

        print('test_isnumber ok')

    # @unittest.skip('skip')
    def test_toint(self):

        data = [
            {
                'args': 1,
                'expect': 1,
            },
            {
                'args': '21',
                'expect': 21,
            },
            {
                'args': '',
                'expect': 0,
            },
            {
                'args': '12.212',
                'expect': 12,
            },
            {
                'args': '12.89',
                'expect': 12,
            },

        ]

        for each in data:
            args = each.get('args', '')
            expect = each.get('expect', '')

            self.assertEqual(expect, toint(args))

        print('test_toint ok')