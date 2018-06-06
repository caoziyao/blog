# coding: utf-8

from app.handler.base_handler import BaseHandler

from app.manager import BookManger


class MznvHandler(BaseHandler):
    def get(self):
        manger = BookManger()
        data = manger.get_book_list()
        self.write(data)
