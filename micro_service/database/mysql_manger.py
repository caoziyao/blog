# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/12
@desc:
"""

import pymysql
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import option
from utilities.util import models_to_list, model_to_dict

# # 创建对象的基类:
pymysql.install_as_MySQLdb()
Base = declarative_base()
engine = create_engine(option.mysql_engine)


class MySQLManger(object):
    # _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super(MySQLManger, cls).__new__(cls)
    #     return cls._instance

    def __init__(self):
        # 创建DBSession类型:
        self.session = sessionmaker(bind=engine)

    def load_members(self, model):
        """
        加载数据库字段
        :return:
        """
        # d = {c.name: getattr(model, c.name) for c in model.__table__.columns}
        l = [c.name for c in model.__table__.columns]
        return l

    def filter_data(self, model, data):
        """
        :param model: sql model
        :param data:
        :return:
        """
        d = {}
        for k, v in data.items():
            if k in self.load_members(model):
                d[k] = v
        return d

    def filter_query(self, model, query):
        """
        :param model: SQLAlchemy mdoel
        :param query: dict
        :return:
        """
        f = []

        for k, v in query.items():
            if hasattr(model, k):
                f.append(getattr(model, k) == v)
        return f

    def load_data_one(self, query, order_by=None):
        """
        加载一条数据
        :param keyword:
        :param value:
        :param order_by:
        :return:
        """
        if not isinstance(query, dict):
            raise Exception('query not dict')

        model = self.model

        fq = self.filter_query(model, query)
        res = self.session.query(model).filter(*fq).one()

        d = model_to_dict(res)
        return d

    def load_data_list(self, query):
        """
        加载多条数据
        :param keyword:
        :param value:
        :param order_by:
        :return:
        """
        if not isinstance(query, dict):
            raise Exception('query not dict')

        model = self.model

        fq = self.filter_query(model, query)
        res = self.session.query(model).filter(*fq).all()
        l = models_to_list(res)

        return l

    def add_data(self, data):
        """
        添加数据到数据库
        :param keyword:
        :return:
        """
        if not isinstance(data, dict):
            raise Exception('data not dict')

        session = self.session
        model = self.model

        d = self.filter_data(model, data)
        d.update({
            'create_time': datetime.now(),
            'update_time': datetime.now(),
        })

        session.add(model(**d))
        session.commit()

    def add_data_list(self, data_list):
        """
        添加数据到数据库
        :param keyword:
        :return:
        """
        if not isinstance(data_list, list):
            raise Exception('data_list not dict')

        session = self.session
        model = self.model

        for data in data_list:
            d = self.filter_data(model, data)
            d.update({
                'create_time': datetime.now(),
                'update_time': datetime.now(),
            })

            session.add(model(**d))

        session.commit()
        return True

    def update_data(self, keyword):
        """
        更新数据库数据
        :param keyword:
        :return:
        """
        pass

    def delete_data(self, query):
        """
        删除数据库数据
        :param keyword:
        :return:
        """
        model = self.model
        session = self.session

        fq = self.filter_query(model, query)
        session.query(model).filter(*fq).delete()

    def fetch_rows(self, query=None, condition=None, order_by=None, fetchone=False, limit=[]):
        """
        加载多条数据
        :param query: 不指定 query 字段, 将返回所有*字段
        :param condition: 不指定 condition 字段, 将条件 where = 1
        :param order_by: 不指定 order, 将不进行排序
        :param fetchone:  不指定 fetchone, 将返回多条数据
        :param limit:  不指定 limit, 返回全部数据
        :return:
        """

        return False
