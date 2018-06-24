# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/6 
@desc:
"""

import grpc
from demo2 import data_pb2

from example.demo2 import data_pb2_grpc

# _HOST = 'localhost'
# _PORT = '8080'

_HOST = 'localhost'
_PORT = '5672'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    response = client.DoFormat(data_pb2.Data(text='hello,world!'))
    print("received: " + response.text)

if __name__ == '__main__':
    run()
