# coding: utf-8

from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
# from .base_model import BaseModel
from app.database import Base

class ArticleModel(Base):
    # 表的名字:
    __tablename__ = 'tb_article'

    # 表的结构:
    id = Column(Integer, primary_key=True, doc="主键id")
    name = Column(String(255), doc='书名')
    path = Column(String(255), doc='路径')
    update_time = Column(DateTime, doc='创建时间')
    create_time = Column(DateTime, doc='创建时间')
    #
    book_id = Column(Integer, ForeignKey('tb_book.id'))
    # 虚拟关系
    tb_book = relationship('BookModel', foreign_keys=[book_id])


    def to_json(self):

        d = {
            'id': self.id,
            'name': self.name,
            'path': self.path,
            'book_name': self.tb_book.name,
        }
        return d
