# coding: utf-8

from app.handler.base_handler import BaseHandler


class TestHandler(BaseHandler):
    def get(self):
        self.write('abcd')
