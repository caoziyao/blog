# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/10 
@desc:
"""
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text
from notebook.database.init_mydql import Base


class UserModel(Base):
    __tablename__ = 'tb_user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    username = Column(String(255))
    password = Column(String(255))

    update_time = Column(DateTime, default=datetime.now)
    add_time = Column(DateTime, default=datetime.now)

    def to_json(self):
        d = {
            c.name: getattr(self, c.name, None) for c in self.__table__.columns
        }

        return d