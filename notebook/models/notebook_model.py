# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""

import pymongo
import logging
import traceback
from .base_model import BaseModel

logger = logging.getLogger('dblog')


class NoteBookModel(BaseModel):
    """
    笔记本
    """

    def __init__(self):
        self.coll_name = 'tb_notebook'
        super(NoteBookModel, self).__init__(self.coll_name)

    def ensure_index(self):
        """
        添加索引
        :return:
        """
        result = self.col.ensure_index([('title', pymongo.ASCENDING)], unique=True)
        return result

    def notebook_one_by_query(self, query, fields=None):
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

    def notebook_by_query(self, query, fields=None):
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

    def add_notebook(self):
        """
        添加数据到数据库
        :param keyword:
        :return:
        """
        res = self.add_data()
        return res

    def update_notebook(self, spec):
        """
        将内存中的项目数据以更新的方式存入数据库
        :return:
        """
        res = self.update_data(spec)
        return res

    def delete_notebook(self, query):
        """
         将数据从数据库中删除
        :return:
        """
        result = self.delete_data(query)
        return result

    def delete_one_notebook(self, query):
        """
         将数据从数据库中删除一条数据
        :return:
        """
        result = self.delete_one_data(query)
        return result