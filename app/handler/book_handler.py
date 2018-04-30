# coding: utf-8

import os
import json
import datetime
from app.utils.const import WikiRoot, ignore_file
from .base_handler import BaseHandler
from app.model import Node, Tree

from app.dbbase import DBSession, BookModel, ArticleModel

class BookHandler(BaseHandler):
    def get(self, action=''):
        print('get action', action)
        tree_route = {
            'get_book_list': self.get_book_list,
        }
        f = tree_route.get(action, None)
        if f is not None:
            f()

    def get_book_list(self):
        # 创建Session:
        session = DBSession()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        books = session.query(BookModel).all()
        articles = session.query(ArticleModel).join(BookModel).filter(BookModel.id == ArticleModel.book_id)
        res = articles.all()
        # 打印类型和对象的name属性:
        temp = []
        books = {}
        for x in res:
            tb_book = x.tb_book
            book_name = tb_book.name
            article = x.to_json()
            books.setdefault(book_name, []).append(article)

        for k, v in books.items():
            d = {
                'name': k,
                'article': v
            }
            temp.append(d)


        print('type:', type(res), temp)

        # 关闭Session:
        session.close()

        self.write(json.dumps(temp))