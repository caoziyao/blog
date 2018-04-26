# coding: utf-8

import os
import tornado.ioloop
import tornado.web
from app.routes import routes


def make_app():
    setting = dict(
        static_path=os.path.join(os.path.dirname(__file__), 'app', "static"),
        template_path=os.path.join(os.path.dirname(__file__), 'app', "templates"),
        debug='True',
    )
    print(setting)
    return tornado.web.Application(routes, **setting)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
