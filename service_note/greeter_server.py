# coding: utf-8
import grpc
import time
from concurrent import futures

from proto import notebook_pb2, notebook_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = '127.0.0.1'
_PORT = '8004'

class Greeter(notebook_pb2_grpc.NotebookServicer):
	# 工作函数
    def GetNotebookInfo(self, request, context):
        print('in grrrettt')
        return notebook_pb2.NotebookResponse(id=1, name="hello", age=12, title=['abc'])


def serve():
    # gRPC 服务器
    print('------------[::]:8004--------')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notebook_pb2_grpc.add_NotebookServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8004')
    # server.add_insecure_port(_HOST + ':' + _PORT)
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
