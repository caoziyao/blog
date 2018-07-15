# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2013-2018
@contact: wyzycao@gmail.com
@time: 2018/5/31
@desc:
"""

from common.logger import dblog
from micro_services.user.models import UserModel
# from .note_manger import NoteManager
from database import MySQLManger
from utilities.util import models_to_list, model_to_dict


class UserManager(MySQLManger):
    _users = {}

    def __init__(self):
        self.db_name = 'db_user'
        self.model = UserModel
        super(UserManager, self).__init__()


    def add_user(self, data):
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

    def add_user_list(self, data_list):
        """
        新建多个到数据库
        :param data:
        :return:
        """
        self.add_user_list(data_list)
        return True

    def user_from(self, query):
        """
        返回 user list
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

    def user_one_from(self, query):
        """
        返回单个 user
        :param query:
        :return: dict
        """
        l = self.load_data_list(query)
        return l

    def is_exit_books(self, query):
        """
        查询是否存在该笔记
        :param title:
        :param user_id:
        :return:
        """
        if not isinstance(query, dict):
            raise Exception('query not dict')

        ext = self.user_one_from(query)

        return True if ext else False

    def delete_one_user(self, query):
        """
        删除笔记本，如果存在笔记也一起删除
        :param _id:
        :return:
        """
        if self.is_exit_books(query):
            self.delete_one_user(query)
            return True
        else:
            return False

# import pymongo
# from bson import ObjectId
# import hashlib
# import logging
# from datetime import datetime
# from micro_services.user.models import UserModel
# from database import MongoManger
# from utilities.util import to_objectid
#
# logger = logging.getLogger('dblog')
#
#
# class UserManager(object):
#     _users = {}
#
#     def __init__(self):
#         super(UserManager, self).__init__()
#
#     def new_user(self):
#         """
#         创建一个 model 实例
#         :return:
#         """
#         model = UserModel()
#         result = model.ensure_index()
#         return model
#
#     def get_user(self, _id, user_id):
#         """
#         返回一个已存在的 model 实例
#         :return:
#         """
#         query = {
#             '_id': to_objectid(_id),
#             'user_id': user_id,
#         }
#         fields = ['_id']
#         user = UserModel()
#         data = user.user_one_by_query(query, fields)
#         if data:
#             user.document = data
#             return user
#         else:
#             return None
#
#     def is_exit_user(self, user_id):
#         """
#         查询是否存在该用户
#         :param title:
#         :param user_id:
#         :return:
#         """
#         query = {
#             'user_id': user_id,
#         }
#         fields = ['_id', 'user_id']
#         user = UserModel()
#         exit_user = user.user_one_by_query(query, fields)
#         return True if exit_user else False
#
#     def user_by_userid(self, user_id):
#         """
#         获取用户
#         :param user_id:
#         :return:
#         """
#         query = {
#             'user_id': user_id
#         }
#         fields = ['user_id', 'create_time', 'update_time']
#         user = UserModel()
#         res = user.user_one_by_query(query, fields)
#         return res
