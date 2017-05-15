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
        # output_path = os.path.join(project_name, 'output')
        output_path = os.path.join(project_name, 'themes','notmyidea', 'templates')
        template_path = output_path
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)

        self.map = self.url_map()

    def url_map(self):
        """
        自动添加路由
        :return:
        """
        project_name = CONF['project_name']
        output_path = os.path.join(project_name, 'output')


        filelist = set()
        for file in os.listdir(output_path):
            print('file', file)
            filepath = os.path.join(output_path, file)
            if os.path.isfile(filepath):
                name = os.path.splitext(file)[0]
                filelist.add(name)

        #  samples/themes/notmyidea/templates/index.html
        rules = [Rule('/{}'.format(name), endpoint='{}'.format(name)) for name in list(filelist)]
        # index_path = os.path.join(project_name, 'themes', 'notmyidea', 'templates', 'index')
        rules.append(Rule('/', endpoint='index'))

        return Map(rules)


    def dispatch_request(self, request):
        adapter = self.map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()

            print('endpoint', endpoint)
            htmlfile = endpoint + '.html'
            return self.render_template(htmlfile, **values)
        except HTTPException as e:
            return e


    def is_valid_url(url):
        pass


    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')


    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
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

