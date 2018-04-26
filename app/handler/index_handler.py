# coding: utf-8

from .base_handler import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')
        # self.write("Hello, world")
        # self.finish()
