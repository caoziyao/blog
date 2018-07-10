# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""

import copy
import logging
import traceback
from bson import ObjectId
from datetime import datetime
from database import mongodb
from utilities.util import utc_to_localtime


class BaseModel(object):
    def __init__(self, table_name):
        self._table_name = table_name
        self._document = {}
        self.db = mongodb
        self.col = self.get_collection(table_name)

    def get_collection(self, coll_name):
        try:
            coll = self.db[coll_name]
            return coll
        except Exception as e:
            logging.error(traceback.format_exc())

    def need_fields_dict(self, fields):
        """
        需要查询的字段
        :param fields: list
        :return:
        """
        d = {}
        if isinstance(fields, list):
            for each in fields:
                conf = {
                    each: 1,
                }
                d.update(conf)
        return d

    def load_one_data(self, query, fields):
        """
        加载一条数据
        :param query: 查询条件 {'id': 123456}
        :param fields: 返回的字段 {'field': 1}
        :param order_by:
        :return:
        """
        res = self.col.find_one(query, fields)
        return res

    def load_data(self, query, fields, order_by=None):
        """
        加载数据
        :param query: 查询条件 {'id': 123456}
        :param fields: 返回的字段 {'field': 1}
        :param order_by: 排序 {'date': -1}
        :return:
        """
        if isinstance(order_by, dict):
            res = self.col.find(query, fields).sort(order_by)
        else:
            res = self.col.find(query, fields)
        return res

    def add_data(self):
        """
        添加数据到数据库
        :param keyword:
        :return:
        """
        data = self.document
        if data:
            _id = self.col.insert(data)
            return _id
        else:
            return None

    def update_data(self, spec):
        """
        更新数据库数据
        :param spec: 要更新的数据
        :param document: 要更新的最新数据
        :return:
        """

        document = copy.deepcopy(self.document)
        document.pop('_id')
        res = self.col.update(spec, {'$set': document})
        return res

    def delete_data(self, query):
        """
        删除数据库数据
        :param query: 删除条件
        :return:
        """
        result = self.col.delete_many(query)
        return result

    def delete_one_data(self, query):
        """
        删除数据库数据一条数据
        :param query: 删除条件
        :return:
        """
        result = self.col.delete_one(query)
        return result

    @property
    def document(self):
        """
        取得数据字典
        :return:
        """
        return self._document

    @document.setter
    def document(self, value):
        self._document = value

    def __getattr__(self, item):
        """
        以类属性的方式访问数据字典
        :param item:
        :return:
        """
        if item in self._document:
            return self._document[item]
        return None

    def mongodb_to_dict(self, res_db):
        """
        mongodb 类型转换为 python 类型
        :param res_db: mongodb dict
        :return: python dict
        """
        if isinstance(res_db, dict):
            for k, v in res_db.items():
                if isinstance(v, ObjectId):
                    res_db[k] = str(v)
                elif isinstance(v, datetime):
                    _format = '%Y-%m-%d %H:%M:%S'
                    v = utc_to_localtime(v)
                    res_db[k] = v.strftime(_format)
                elif isinstance(v, list):
                    res_db[k] = self.mongodb_to_list(v)
        return res_db

    def mongodb_to_list(self, res_db_list):
        """
        mongodb 类型转换为 python 类型
        :param res_db_list: mongodb list
        :return: python list
        """
        res = []
        if isinstance(res_db_list, list):
            for each in res_db_list:
                d = self.mongodb_to_dict(each)
                res.append(d)
        return res

    def mongo_cursor_to_list(self, cursor):
        """
        find 得到的是游标，需要转换为 dict
        :return:
        """
        l = []
        for each in cursor:
            d = {}
            k = self.mongodb_to_dict(each)
            for key, value in k.items():
                d[key] = value
            l.append(d)
        return l