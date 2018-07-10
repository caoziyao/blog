# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
import grpc
from .app.service.api_service import IndexService
from .app_run import make_app, app_config

from concurrent import futures
from config import option
from proto import api_pb2_grpc, api_pb2


class ApiService(object):

    def __init__(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=option.max_workers))
        api_pb2_grpc.add_ApiServicer_to_server(IndexService(), server)

        ins_port = '[::]:{}'.format(str(option.api_srv_port))
        server.add_insecure_port(ins_port)
        server.start()

    def run(self):
        config = app_config()
        app = make_app()
        app.run(**config)
