# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/13 
@desc:
"""
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# # 创建对象的基类:
# pymysql.install_as_MySQLdb()
# Base = declarative_base()
#
#
class BaseModel(object):

    pass
    # @property
    # def members(self):
    #     """
    #     字段名称
    #     :return:
    #     """
    #     model = self.model
    #     # d = {c.name: getattr(model, c.name) for c in model.__table__.columns}
    #     l = [c.name for c in model.__table__.columns]
    #     return l
