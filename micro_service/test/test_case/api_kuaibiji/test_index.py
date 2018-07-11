# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
from test.test_case.base import BaseCase
from utilities.util import ucode_json

class FlaskrTestCase(BaseCase):

    def test_index(self):
        print('==========test_index=========')
        rv = self.app.get('/')
        data = rv.data.decode()
        assert 'hello' in data

    def test_user(self):
        print('==========test_user=========')
        # oMNol0Yk9XeI_0jHsYuFgFsQ2h6s
        rv = self.app.get('/user/user_info?user_id=121')
        data = rv.data.decode()
        # print('data', data)
        assert 'data' in data

    def test_notebook_info(self):
        print('==========test_notebook info=========')
        # oMNol0Yk9XeI_0jHsYuFgFsQ2h6s
        rv = self.app.get('/notebook/notebook?user_id=oMNol0Yk9XeI_0jHsYuFgFsQ2h6s')
        data = rv.data.decode()
        print('data', ucode_json(data), type(data))
        assert 'data' in data

    def test_weixin_login(self):
        print('==========test_weixin_login=========')
        # oMNol0Yk9XeI_0jHsYuFgFsQ2h6s
        rv = self.app.get('/user/weixin_login?user_id=oMNol0Yk9XeI_0jHsYuFgFsQ2h6s')
        data = rv.data.decode()
        # print('data', ucode_json(data), type(data))
        # assert 'data' in data

    def test_weixin_logout(self):
        print('==========test_weixin_logout=========')
        # oMNol0Yk9XeI_0jHsYuFgFsQ2h6s
        rv = self.app.get('/user/weixin_logout?user_id=oMNol0Yk9XeI_0jHsYuFgFsQ2h6s')
        data = rv.data.decode()
        # print('data', ucode_json(data), type(data))
        # assert 'data' in data

