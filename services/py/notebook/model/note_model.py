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


class NoteModel(Base):
    __tablename__ = 'tb_note'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    notebook_id = Column(Integer)
    name = Column(String(255))
    content = Column(Text)

    update_time = Column(DateTime, default=datetime.now)
    add_time = Column(DateTime, default=datetime.now)

    def to_json(self):
        d = {
            c.name: getattr(self, c.name, None) for c in self.__table__.columns
        }

        return d