# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import myworld_pb2 as myworld__pb2


class MyGreeterStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DoSomething = channel.unary_unary(
                '/MyGreeter/DoSomething',
                request_serializer=myworld__pb2.SomeRequest.SerializeToString,
                response_deserializer=myworld__pb2.SomeReply.FromString,
                )


class MyGreeterServicer(object):
    """Missing associated documentation comment in .proto file"""

    def DoSomething(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyGreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DoSomething': grpc.unary_unary_rpc_method_handler(
                    servicer.DoSomething,
                    request_deserializer=myworld__pb2.SomeRequest.FromString,
                    response_serializer=myworld__pb2.SomeReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MyGreeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyGreeter(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def DoSomething(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyGreeter/DoSomething',
            myworld__pb2.SomeRequest.SerializeToString,
            myworld__pb2.SomeReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
