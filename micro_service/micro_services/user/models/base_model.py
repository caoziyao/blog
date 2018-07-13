# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""


from database import MongoManger

class BaseModel(object):
    pass
    # def __init__(self, table_name):
    #     self._table_name = table_name
    #     self._document = {}
    #     self.db = MongoManger().db
    #     self.col = self.get_collection(table_name)
    #
