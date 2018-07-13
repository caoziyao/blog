# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/13 
@desc:
"""

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from .base_model import BaseModel
from database import Base


class NoteModel(Base, BaseModel):
    __tablename__ = 'tb_note'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    update_time = Column(DateTime, default=datetime.utcnow)
    create_time = Column(DateTime, default=datetime.utcnow)