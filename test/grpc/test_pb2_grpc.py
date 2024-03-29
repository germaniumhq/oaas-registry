# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test.grpc.test_pb2 as test__pb2


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
            "/TestService/ping",
            request_serializer=test__pb2.Ping.SerializeToString,
            response_deserializer=test__pb2.Pong.FromString,
        )
        self.ping_copy = channel.unary_unary(
            "/TestService/ping_copy",
            request_serializer=test__pb2.Ping.SerializeToString,
            response_deserializer=test__pb2.Pong.FromString,
        )
        self.ping_exception = channel.unary_unary(
            "/TestService/ping_exception",
            request_serializer=test__pb2.Ping.SerializeToString,
            response_deserializer=test__pb2.Pong.FromString,
        )


class TestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ping_copy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ping_exception(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    @staticmethod
    def add_to_server(servicer, server):
        rpc_method_handlers = {
            "ping": grpc.unary_unary_rpc_method_handler(
                servicer.ping,
                request_deserializer=test__pb2.Ping.FromString,
                response_serializer=test__pb2.Pong.SerializeToString,
            ),
            "ping_copy": grpc.unary_unary_rpc_method_handler(
                servicer.ping_copy,
                request_deserializer=test__pb2.Ping.FromString,
                response_serializer=test__pb2.Pong.SerializeToString,
            ),
            "ping_exception": grpc.unary_unary_rpc_method_handler(
                servicer.ping_exception,
                request_deserializer=test__pb2.Ping.FromString,
                response_serializer=test__pb2.Pong.SerializeToString,
            ),
        }
        generic_handler = grpc.method_handlers_generic_handler(
            "TestService", rpc_method_handlers
        )
        server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ping(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/TestService/ping",
            test__pb2.Ping.SerializeToString,
            test__pb2.Pong.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ping_copy(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/TestService/ping_copy",
            test__pb2.Ping.SerializeToString,
            test__pb2.Pong.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ping_exception(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/TestService/ping_exception",
            test__pb2.Ping.SerializeToString,
            test__pb2.Pong.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
