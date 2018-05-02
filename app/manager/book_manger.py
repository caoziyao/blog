# coding: utf-8

import json
from app.model import Node, Tree,  BookModel, ArticleModel
from app.database import DBSession, redis_client

class BookManger(object):

    def __init__(self):
        pass

    def list_canche(self):
        r = redis_client
        data = r.hget("hash1", "k1")
        return data

    def get_book_list(self):
        r = redis_client
        data = self.list_canche()
        if not data:
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

            data = json.dumps(temp).encode()
            r.hset("hash1", "k1", data)
        data = data.decode()

        return data