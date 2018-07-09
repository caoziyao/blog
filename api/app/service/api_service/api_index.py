# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
from proto import api_pb2
from proto import api_pb2_grpc

class IndexService(api_pb2_grpc.ApiServicer):

    def index(self, request, context):
        """
        api index
        """
        metadata = dict(context.invocation_metadata())
        data = request.data
        res = dict(
            data=data,
        )
        return api_pb2.IndexResponse(**res)

