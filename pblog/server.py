# coding: utf-8

import os
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
from pblog.generator import CONF


class Shortly(object):


    def __init__(self):
        project_name = CONF['project_name']
        output_path = os.path.join(project_name, 'output')
        template_path = output_path
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)


    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')


    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.render_template('hello.html', url='sss')
        return response(environ, start_response)


    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app():
    app = Shortly()
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
    })
    return app


def run_server():
    """
    启动服务
    :return:
    """
    from werkzeug.serving import  run_simple
    app = create_app()
    run_simple('127.0.0.1', 3000, app, use_debugger=True, use_reloader=True)

