"""
如何写一个 todo
或者说，如何规划新项目

1，写出 model
2，写出路由
3，写 html 模板\
"""

from response import template, response_with_headers
from models import Todo
from utils import log

# start_line = 'HTTP/1.x 200 IK\r\n'
# header = 'Content-Type: text/html\r\n'

headers = {
    'Content-Type': 'text/html',
}

def route_index(request):
    """
    Todo 首页
    """
    header = response_with_headers(headers)
    todos = Todo.all()
    log('todos:', todos)

    def todo_tag(t):
        return '<p>{} {} @{}<a href="/todo/complete?id={}">完成</a></p>'.format(
            t.id,
            t.content,
            t.created_time,
            t.id,
        )

    todo_html = ''
    if todos != None:
        todo_html = '\n'.join([todo_tag(t) for t in todos])

    body = template('todo_index.html', todos=todo_html)


    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')

def route_add(request):
    # headers = {
    #     'Content-Type': 'text/html',
    # }
    # 创建Todo
    # form = request.form()
    # o = Todo(form)
    # o.save()
    # return
    r = b'HTTP/1.x 200 FOUND\r\n\r\n<h1>Hello aaa FOUND</h1>'

    return r



routes = {
    '/todo': route_index,
    '/todo/add': route_add,
}