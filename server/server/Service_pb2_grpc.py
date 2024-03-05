# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Service_pb2 as Service__pb2


class MainFunctionsStub(object):
    """
    message Product{ //ESTA ES LA PREGUNTA DEL CLIENTE
    int32 id_product = 1;
    }

    message TransactionResponse{ //ESTA ES LA RESPUESTA DEL SERVIDOR
    int32 status_code = 1;
    }

    service ProductService{
    //AddProduct es inventado
    rpc AddProduct(Product) returns (TransactionResponse) {}
    }

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login = channel.unary_unary(
                '/MainFunctions/login',
                request_serializer=Service__pb2.Credentials.SerializeToString,
                response_deserializer=Service__pb2.OperationResponse.FromString,
                )
        self.logout = channel.unary_unary(
                '/MainFunctions/logout',
                request_serializer=Service__pb2.Credentials.SerializeToString,
                response_deserializer=Service__pb2.OperationResponse.FromString,
                )
        self.search = channel.unary_unary(
                '/MainFunctions/search',
                request_serializer=Service__pb2.Credentials.SerializeToString,
                response_deserializer=Service__pb2.OperationResponse.FromString,
                )
        self.index = channel.unary_unary(
                '/MainFunctions/index',
                request_serializer=Service__pb2.Credentials.SerializeToString,
                response_deserializer=Service__pb2.OperationResponse.FromString,
                )


class MainFunctionsServicer(object):
    """
    message Product{ //ESTA ES LA PREGUNTA DEL CLIENTE
    int32 id_product = 1;
    }

    message TransactionResponse{ //ESTA ES LA RESPUESTA DEL SERVIDOR
    int32 status_code = 1;
    }

    service ProductService{
    //AddProduct es inventado
    rpc AddProduct(Product) returns (TransactionResponse) {}
    }

    """

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MainFunctionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=Service__pb2.Credentials.FromString,
                    response_serializer=Service__pb2.OperationResponse.SerializeToString,
            ),
            'logout': grpc.unary_unary_rpc_method_handler(
                    servicer.logout,
                    request_deserializer=Service__pb2.Credentials.FromString,
                    response_serializer=Service__pb2.OperationResponse.SerializeToString,
            ),
            'search': grpc.unary_unary_rpc_method_handler(
                    servicer.search,
                    request_deserializer=Service__pb2.Credentials.FromString,
                    response_serializer=Service__pb2.OperationResponse.SerializeToString,
            ),
            'index': grpc.unary_unary_rpc_method_handler(
                    servicer.index,
                    request_deserializer=Service__pb2.Credentials.FromString,
                    response_serializer=Service__pb2.OperationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MainFunctions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MainFunctions(object):
    """
    message Product{ //ESTA ES LA PREGUNTA DEL CLIENTE
    int32 id_product = 1;
    }

    message TransactionResponse{ //ESTA ES LA RESPUESTA DEL SERVIDOR
    int32 status_code = 1;
    }

    service ProductService{
    //AddProduct es inventado
    rpc AddProduct(Product) returns (TransactionResponse) {}
    }

    """

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MainFunctions/login',
            Service__pb2.Credentials.SerializeToString,
            Service__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MainFunctions/logout',
            Service__pb2.Credentials.SerializeToString,
            Service__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MainFunctions/search',
            Service__pb2.Credentials.SerializeToString,
            Service__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MainFunctions/index',
            Service__pb2.Credentials.SerializeToString,
            Service__pb2.OperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
