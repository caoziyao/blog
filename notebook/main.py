# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc: notebook 服务
"""
import time
import grpc
from concurrent import futures
from proto import notebook_pb2_grpc
from config import option
from service import Greeter


def delay(server):
    try:
        while True:
            time.sleep(option.day)
    except KeyboardInterrupt:
        server.stop(0)

def main():
    # gRPC 服务器
    print('host', option.host)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=option.max_workers))
    notebook_pb2_grpc.add_NotebookServicer_to_server(Greeter(), server)
    # server.add_insecure_port('0.0.0.0:8004')

    ins_port = '[::]:{}'.format(str(option.port))
    server.add_insecure_port(ins_port)
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    delay(server)


if __name__ == '__main__':
    main()
