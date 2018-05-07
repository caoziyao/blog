# coding: utf-8

import json
from app.model import NodeModel, TreeModel,  BookModel, ArticleModel
from app.database import DBSession
from app.cache import redis_client
from app.utils import cache_func
from app.config import Config

class BookManger(object):

    def __init__(self):
        pass

    @cache_func(Config.redis_cache_time)
    def get_book_list(self):

        # 创建Session:
        session = DBSession()
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        books = session.query(BookModel).all()
        articles = session.query(ArticleModel).join(BookModel).filter(BookModel.id == ArticleModel.book_id)
        res = articles.all()
        # 打印类型和对象的name属性:
        data = []
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
            data.append(d)

        print('read data:')

        # 关闭Session:
        session.close()

        data = json.dumps(data)

        return data