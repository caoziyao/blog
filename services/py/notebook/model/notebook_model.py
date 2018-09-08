# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from notebook.database.init_mydql import Base


class NotebookModel(Base):
    __tablename__ = 'tb_notebook'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def to_json(self):
        d = {
            c.name: getattr(self, c.name, None) for c in self.__table__.columns
        }

        return d