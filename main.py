# coding: utf-8

import os
import tornado.ioloop
import tornado.web
from app.handler import handlers
from tornado.options import define, options, parse_config_file
from app.config import Config

# redis-server /usr/local/etc/redis/conf/redis6400.conf

def make_app():
    setting = dict(
        static_path=os.path.join(os.path.dirname(__file__), 'app', "static"),
        template_path=os.path.join(os.path.dirname(__file__), 'app', "templates"),
        debug='True',
    )
    print(setting)
    return tornado.web.Application(handlers, **setting)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
