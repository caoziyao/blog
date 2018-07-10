# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2013-2018
@contact: wyzycao@gmail.com
@time: 2018/5/31
@desc:
"""
import pymongo
from .base_model import BaseModel


class UserModel(BaseModel):
    """
    用户信息
    user_id, user_name, user_passwd,
    """

    def __init__(self):
        self.coll_name = 'tb_user'
        super(UserModel, self).__init__(self.coll_name)
        self.col = self.get_collection(self.coll_name)

    def ensure_index(self):
        """
        添加索引
        :return:
        """
        self.col.ensure_index([('user_id', pymongo.ASCENDING)], unique=True)

    def user_one_by_query(self, query, fields=None):
        """
        加载多条数据
        :param query: 查询条件
        :param fields: 是列表 []
        :return:
        """
        need_fields = self.need_fields_dict(fields)
        res = self.load_one_data(query, need_fields)
        if res:
            l = self.mongodb_to_dict(res)
            return l
        else:
            return {}

    def user_by_query(self, query, fields=None):
        """
        加载多条数据
        :param query: 查询条件
        :param fields: 是列表 []
        :return:
        """
        need_fields = self.need_fields_dict(fields)
        res = self.load_data(query, need_fields)
        if res:
            l = self.mongo_cursor_to_list(res)
            return l
        else:
            return []

    def add_user(self):
        """
        添加数据到数据库
        :param keyword:
        :return:
        """
        res = self.add_data()
        return res

    def update_user(self, spec):
        """
        将内存中的项目数据以更新的方式存入数据库
        :return:
        """
        res = self.update_data(spec)
        return res
