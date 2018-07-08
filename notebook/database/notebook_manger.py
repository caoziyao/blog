# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""

import pymongo
from datetime import datetime
import logging
from bson import ObjectId
from models import NoteBookModel
# from .note_manger import NoteManager
from utilities.util import to_objectid

logger = logging.getLogger('dblog')


class NoteBookManager(object):
    _users = {}

    def __init__(self):
        super(NoteBookManager, self).__init__()

    def new_notebook(self):
        """
        创建一个 model 实例
        :return:
        """
        model = NoteBookModel()
        result = model.ensure_index()
        return model

    def get_notebook(self, _id, user_id):
        """
        返回一个已存在的 model 实例
        :return:
        """
        query = {
            '_id': to_objectid(_id),
            'user_id': user_id,
        }
        fields = ['_id']
        notebook = NoteBookModel()
        data = notebook.notebook_one_by_query(query, fields)
        if data:
            notebook.document = data
            return notebook
        else:
            return None

    def is_exit_books(self, user_id, title):
        """
        查询是否存在该笔记
        :param title:
        :param user_id:
        :return:
        """
        query = {
            'user_id': user_id,
            'title': title,
        }
        fields = ['_id']
        notebook = NoteBookModel()
        exit_books = notebook.notebook_by_query(query, fields)
        return True if exit_books else False

    def is_exit_books_by_id(self, _id, user_id):
        """
        查询是否存在该笔记
        :param _id:
        :return:
        """
        query = {
            '_id': to_objectid(_id),
            'user_id': user_id,
        }
        fields = ['_id']
        notebook = NoteBookModel()
        exit_books = notebook.notebook_one_by_query(query, fields)
        return True if exit_books else False

    def notebooks_by_userid(self, user_id):
        """
        获取用户的所有 笔记本
        :param user_id:
        :return:
        """
        query = {
            'user_id': user_id
        }
        fields = ['title', '_id', 'summary', 'image', 'user_id']
        notebook = NoteBookModel()
        res = notebook.notebook_by_query(query, fields)
        return res

    def delte_one_notebook(self, _id, user_id):
        """
        删除笔记本，如果存在笔记也一起删除
        :param _id:
        :return:
        """
        query = {
            '_id': to_objectid(_id),
            'user_id': user_id,
        }
        notebook = NoteBookModel()
        result = notebook.delete_one_notebook(query)

        # note_manager = NoteManager()
        # note_manager.delete_note_by_bookid(_id, user_id)
