# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
import grpc
from concurrent import futures
from app.config import option
from app.service.api_service import IndexService

from proto import api_pb2_grpc, api_pb2


def service_wrapper():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=option.max_workers))
    api_pb2_grpc.add_ApiServicer_to_server(IndexService(), server)

    ins_port = '[::]:{}'.format(str(option.port))
    server.add_insecure_port(ins_port)
    server.start()