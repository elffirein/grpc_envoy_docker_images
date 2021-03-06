# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sample_pb2 as sample__pb2


class SampleRPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Save = channel.unary_unary(
                '/sample.SampleRPC/Save',
                request_serializer=sample__pb2.SaveReq.SerializeToString,
                response_deserializer=sample__pb2.SaveRes.FromString,
                )
        self.Get = channel.unary_unary(
                '/sample.SampleRPC/Get',
                request_serializer=sample__pb2.GetReq.SerializeToString,
                response_deserializer=sample__pb2.GetRes.FromString,
                )


class SampleRPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SampleRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Save': grpc.unary_unary_rpc_method_handler(
                    servicer.Save,
                    request_deserializer=sample__pb2.SaveReq.FromString,
                    response_serializer=sample__pb2.SaveRes.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=sample__pb2.GetReq.FromString,
                    response_serializer=sample__pb2.GetRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sample.SampleRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SampleRPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sample.SampleRPC/Save',
            sample__pb2.SaveReq.SerializeToString,
            sample__pb2.SaveRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sample.SampleRPC/Get',
            sample__pb2.GetReq.SerializeToString,
            sample__pb2.GetRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
