# coding: utf-8

from tornado import web
from app.handler import MainHandler, TestHandler, TreeHandler

routes = [
    (r"/", MainHandler),
    (r"/api/", TestHandler),
    # (r'/api/get/tree', TreeHandler),
    web.URLSpec(r"/api/tree/([^/]+)", TreeHandler, name="tree"),
]