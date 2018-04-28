# coding: utf-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, x-token")
        # self.set_header("Access-Control-Allow-Credentials", True)
