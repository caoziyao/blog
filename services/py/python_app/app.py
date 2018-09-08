# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/7 
@desc:
"""
import sys
import os

# sys.path.append(os.path.join(os.path.abspath(__file__), '..', '..'))
# print(os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..')))
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from python_app import sidecar
from jsonrpc import JSONRPCResponseManager, dispatcher
# from jsonrpc.jsonrpc import JSONRPCRequest
# from jsonrpc.
# JSONRPC20Request.han

import uuid

service = {
    "name": "go.micro.srv.pyapp",
    "nodes": [{
        "id": "go.micro.srv.greeter-" + str(uuid.uuid4()),
        "address": "srv-pyapp",
        "port": 4000,
    }],
}


@Request.application
def application(request):
    print('s,')
    dispatcher["Say.Hello"] = lambda s: "greeting=" + s["name"] + "!"
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    s = Response(response.json, mimetype='application/json')
    return s


class AppPyService(object):

    def run(self):
        sidecar.register(service)
        run_simple('0.0.0.0', 4000, application)
        sidecar.deregister(service)


if __name__ == '__main__':
    app = AppPyService()
    app.run()

#
# from concurrent import futures
# import time
#
# from proto import hello_pb2
# from proto import hello_pb2_grpc
#
# _ONE_DAY_IN_SECONDS = 60 * 60 * 24
#
#
# class Greeter(hello_pb2_grpc.GreeterServicer):
#     # 工作函数
#     def SayHello(self, request, context):
#         return hello_pb2.HelloReply(message='Hello, %s!' % request.name)
#
#
# class AppHelloService(object):
#
#     def run(self):
#
#         # gRPC 服务器
#         server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#         hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
#         # server.add_insecure_port('[::]:8007')
#         # Opens an insecure port for accepting RPCs
#         server.add_insecure_port('[::]:8009')
#         server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
#         try:
#             while True:
#                 time.sleep(_ONE_DAY_IN_SECONDS)
#         except KeyboardInterrupt:
#             server.stop(0)
