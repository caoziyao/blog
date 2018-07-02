# coding: utf-8

from __future__ import print_function

import grpc

from proto import notebook_pb2, notebook_pb2_grpc


def run():
    channel = grpc.insecure_channel('127.0.0.1:8004')
    stub = notebook_pb2_grpc.NotebookStub(channel)
    response = stub.GetNotebookInfo(notebook_pb2.NotebookRequest(name='goodspeed'))
    print("Greeter client received: " + response.name)


if __name__ == '__main__':
    run()
