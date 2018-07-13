# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/14 
@desc:
"""

import logging
from micro_services.notebook.models import NoteModel
# from .note_manger import NoteManager
from database import MySQLManger
from utilities.util import models_to_list, model_to_dict

logger = logging.getLogger('log')


class NoteManager(MySQLManger):
    _users = {}

    def __init__(self):
        super(NoteManager, self).__init__()
        self.model = NoteModel

    def add_note(self, data):
        """
        新建到数据库
        data = {
            name = "hello"
        }
        :return:
        """
        if not isinstance(data, dict):
            raise Exception('data not dict')

        self.add_data(data)
        return True

    def add_note_list(self, data_list):
        """
        新建多个到数据库
        :param data:
        :return:
        """
        self.add_note_list(data_list)
        return True

    def note_from(self, query):
        """
        返回 noteb list
        query: {
            id = 12,
            name = 'boy'
        }
        :return: list
        """
        if not isinstance(query, dict):
            raise Exception('query not dict')

        d = self.load_data_one(query)
        return d

    def note_one_from(self, query):
        """
        返回单个 note
        :param query:
        :return: dict
        """
        l = self.load_data_list(query)
        return l

    def is_exit_note(self, query):
        """
        查询是否存在该笔记
        :param title:
        :param user_id:
        :return:
        """
        if not isinstance(query, dict):
            raise Exception('query not dict')

        ext = self.note_one_from(query)

        return True if ext else False

    def delete_one_note(self, query):
        """
        删除笔记，如果存在笔记也一起删除
        :param _id:
        :return:
        """
        if self.is_exit_note(query):
            self.delete_one_note(query)
            return True
        else:
            return False
