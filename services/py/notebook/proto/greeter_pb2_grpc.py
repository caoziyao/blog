# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import greeter_pb2 as proto_dot_greeter__pb2


class GreeterStub(object):
  """定义服务的API
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Hello = channel.unary_unary(
        '/Greeter/Hello',
        request_serializer=proto_dot_greeter__pb2.HelloRequest.SerializeToString,
        response_deserializer=proto_dot_greeter__pb2.HelloResponse.FromString,
        )


class GreeterServicer(object):
  """定义服务的API
  """

  def Hello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Hello': grpc.unary_unary_rpc_method_handler(
          servicer.Hello,
          request_deserializer=proto_dot_greeter__pb2.HelloRequest.FromString,
          response_serializer=proto_dot_greeter__pb2.HelloResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
