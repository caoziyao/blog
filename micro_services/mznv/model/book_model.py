# coding: utf-8

from sqlalchemy import Column, String, DateTime, Integer

# from .base_model import BaseModel
from app.database import Base


class BookModel(Base):
    # 表的名字:
    __tablename__ = 'tb_book'

    # 表的结构:
    id = Column(Integer, primary_key=True, doc="主键id")
    name = Column(String(255), doc='书名')
    create_time = Column(DateTime, doc='创建时间')
    update_time = Column(DateTime, doc='更新时间')

    def to_json(self):

        d = {
            'id': self.id,
            'name': self.name,
        }
        return d