# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import gnes_pb2 as gnes__pb2


class GnesServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Train = channel.unary_unary(
        '/gnes.GnesService/Train',
        request_serializer=gnes__pb2.BaseMessage.SerializeToString,
        response_deserializer=gnes__pb2.BaseMessage.FromString,
        )
    self.Index = channel.unary_unary(
        '/gnes.GnesService/Index',
        request_serializer=gnes__pb2.BaseMessage.SerializeToString,
        response_deserializer=gnes__pb2.BaseMessage.FromString,
        )
    self.Query = channel.unary_unary(
        '/gnes.GnesService/Query',
        request_serializer=gnes__pb2.BaseMessage.SerializeToString,
        response_deserializer=gnes__pb2.BaseMessage.FromString,
        )


class GnesServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Train(self, request, context):
    """option (rpc_core.method_no_deadline) = true;
    option (rpc_core.service_default_deadline_ms) = 5000;
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Index(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GnesServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Train': grpc.unary_unary_rpc_method_handler(
          servicer.Train,
          request_deserializer=gnes__pb2.BaseMessage.FromString,
          response_serializer=gnes__pb2.BaseMessage.SerializeToString,
      ),
      'Index': grpc.unary_unary_rpc_method_handler(
          servicer.Index,
          request_deserializer=gnes__pb2.BaseMessage.FromString,
          response_serializer=gnes__pb2.BaseMessage.SerializeToString,
      ),
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=gnes__pb2.BaseMessage.FromString,
          response_serializer=gnes__pb2.BaseMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gnes.GnesService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
