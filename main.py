# coding: utf-8

import os
import tornado.ioloop
import tornado.web
from app.handler import handlers
from tornado.options import define, options, parse_config_file
from app.config import Config

# npm run dev
# redis-server /usr/local/etc/redis/conf/redis6400.conf
# sudo nginx -c /usr/local/etc/nginx/nginx.conf

def make_app():
    setting = dict(
        static_path=os.path.join(os.path.dirname(__file__), 'app', "static"),
        template_path=os.path.join(os.path.dirname(__file__), 'app', "templates"),
        debug='True',
        # cookie签名
        cookie_secret={1: 'this is first key', 2: 'this is second key', 3: 'this is third key'},
        # cookie签名版本
        key_version=1,
        # 登录链接
        login_url='/api/user/login',
    )
    print(setting)
    return tornado.web.Application(handlers, **setting)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
