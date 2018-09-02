# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10
@desc:
"""
import time
import grpc
from concurrent import futures
from proto import notebook_pb2_grpc
from config import config
from .services.notebook_service import Greeter
from common.logger import log


class App(object):

    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=config.max_workers))
        notebook_pb2_grpc.add_NotebookServicer_to_server(Greeter(), self.server)
        # server.add_insecure_port('0.0.0.0:8004')

        ins_port = '[::]:{}'.format(str(config.notebook_port))
        self.server.add_insecure_port(ins_port)

    def run(self):
        print('run notebook {}:{}'.format(str(config.notebook_host), str(config.notebook_port)))
        self.server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
        self.delay(self.server)

    def delay(self, server):
        try:
            while True:
                time.sleep(config.day)
        except KeyboardInterrupt:
            self.server.stop(0)
