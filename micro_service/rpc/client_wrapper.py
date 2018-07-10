# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/9 
@desc:
"""
import sys
import grpc
from functools import partial
from config import option


class ServiceClient(object):

    def __init__(self, service_module, stub_name, host, port, timeout=option.timeout_channel):
        self.service_module = service_module
        self.stub_name = stub_name
        self.host = host
        self.port = port
        self.timeout = timeout
        self.stub = None
        self.client()

    def client(self):
        service_module = self.service_module
        stub_name = self.stub_name
        host = self.host
        port = self.port
        timeout = self.timeout

        channel = grpc.insecure_channel('{}:{}'.format(host, port))
        try:
            grpc.channel_ready_future(channel).result(timeout=timeout)
        except grpc.FutureTimeoutError:
            print('Error connecting to server')

        self.stub = getattr(service_module, stub_name)(channel)

    # def __getattr__(self, attr):
    #     return partial(self._wrapped_call, self.stub, attr)
    #
    # # args[0]: stub, args[1]: function to call, args[3]: Request
    # # kwargs: keyword arguments
    # def _wrapped_call(self, *args, **kwargs):
    #     try:
    #         return getattr(args[0], args[1])(
    #             args[2], **kwargs, timeout=self.timeout
    #         )
    #     except grpc.RpcError as e:
    #         print('Call {0} failed with {1}'.format(
    #             args[1], e.code())
    #         )
    #         raise
