# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/3 
@desc:
"""
import unittest
from tests.test_case.base import BaseCase
from notebook.database.notebook_manger import NotebookManger

class TestMysql(BaseCase):

    def test_connect(self):
        """test_connect"""
        m = NotebookManger()
        m.test_demo()
        print('test_connect')
        # m = NoteBookManager()
        # data = {
        #     'name': 'name1'
        # }
        # m.add_notebook(data)
        # print('test_connect')




