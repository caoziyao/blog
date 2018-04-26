# coding: utf-8

from tornado import web
from app.handler import MainHandler, TestHandler

routes = [
    (r"/", MainHandler),
    (r"/api/", TestHandler),
]