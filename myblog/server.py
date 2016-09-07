
# todo 应用

import socket
from utils import log
from models import request
from routes_todo import routes as route_todo
from routes import routes as route_main

def parsed_path(path):
    """
    解析 path
    /todo/add?content=wfssdf
    """
    index = path.find('?')
    if index == -1:
        return path
    path = path.split('?', 1)[0]
    print(path)
    return path

def parsed_start_line(start_line):
    """
    解析 start_line, 并保存在 RequsetData
    """
    method, path, protocol = start_line.split(' ')
    print(method, path, protocol)

    path = parsed_path(path)

    # 保存在 RequsetData
    request.method = method
    request.protocol = protocol
    request.path = path


def parsed_headers(headers):
    """
    解析 headers，并保存在 RequsetData
    Connection: keep-alive
    """
    header = headers.split('\r\n')
    args = {}
    for h in header:
        k, v = h.split(': ')
        args[k] = v
    # print(args)

    # 保存在 requset_data
    request.headers = args


def parsed_request(r):
    """
    解析请求
    """
    headers, body = r.split('\r\n\r\n', 1)
    start_line, headers = headers.split('\r\n', 1)
    parsed_start_line(start_line)
    parsed_headers(headers)

    # 保存在 RequsetData
    request.body = body
    print(body)


def error(request, code=404):
    """
    404
    """
    e = {
        404: b'HTTP/1.x 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>',
    }
    return e.get(code, b'')


def response_by_route():
    """
    初始化路由, 返回 response
    """
    path = request.path

    route = {

    }
    route.update(route_main)
    route.update(route_todo)

    response = route.get(path, error)
    return response(request)


def run(host='', port=3000):
    """
    启动服务器
    """
    s = socket.socket()
    s.bind((host, port))
    while True:
        """
        服务器不断监听客户端请求
        """
        s.listen(3)
        connection, addr = s.accept()

        # 接受请求
        r = connection.recv(1024)
        r = r.decode(encoding='utf-8')

        # 因为 chrome 会发送空请求导致 split 得到空 list
        # 所以这里判断一下防止程序崩溃
        if len(r.split()) < 2:
            continue

        log(r)

        # 解析请求
        parsed_request(r)

        # 初始化路由 route
        response = response_by_route()

        # 发送 response
        connection.sendall(response)

        # 关闭连接
        connection.close()



if __name__ == '__main__':
    config = dict(
        host = '',
        port = 3001
    )
    with open('log.txt', 'w', encoding='utf-8') as f:
        f.write('')
    run(**config)
