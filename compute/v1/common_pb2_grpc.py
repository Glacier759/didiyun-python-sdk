# coding: utf-8 
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from compute.v1 import common_pb2 as compute_dot_v1_dot_common__pb2


class CommonStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.JobResult = channel.unary_unary(
        '/didi.cloud.compute.v1.Common/JobResult',
        request_serializer=compute_dot_v1_dot_common__pb2.JobResultRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_common__pb2.JobResultResponse.FromString,
        )
    self.ListRegionAndZone = channel.unary_unary(
        '/didi.cloud.compute.v1.Common/ListRegionAndZone',
        request_serializer=compute_dot_v1_dot_common__pb2.ListRegionAndZoneRequest.SerializeToString,
        response_deserializer=compute_dot_v1_dot_common__pb2.ListRegionAndZoneResponse.FromString,
        )


class CommonServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def JobResult(self, request, context):
    """获取任务进度
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRegionAndZone(self, request, context):
    """获取产品可用区列表
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommonServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'JobResult': grpc.unary_unary_rpc_method_handler(
          servicer.JobResult,
          request_deserializer=compute_dot_v1_dot_common__pb2.JobResultRequest.FromString,
          response_serializer=compute_dot_v1_dot_common__pb2.JobResultResponse.SerializeToString,
      ),
      'ListRegionAndZone': grpc.unary_unary_rpc_method_handler(
          servicer.ListRegionAndZone,
          request_deserializer=compute_dot_v1_dot_common__pb2.ListRegionAndZoneRequest.FromString,
          response_serializer=compute_dot_v1_dot_common__pb2.ListRegionAndZoneResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'didi.cloud.compute.v1.Common', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
