# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import collections_pb2 as collections__pb2


class CollectionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/qdrant.Collections/Get',
                request_serializer=collections__pb2.GetCollectionInfoRequest.SerializeToString,
                response_deserializer=collections__pb2.GetCollectionInfoResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/qdrant.Collections/List',
                request_serializer=collections__pb2.ListCollectionsRequest.SerializeToString,
                response_deserializer=collections__pb2.ListCollectionsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/qdrant.Collections/Create',
                request_serializer=collections__pb2.CreateCollection.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/qdrant.Collections/Update',
                request_serializer=collections__pb2.UpdateCollection.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/qdrant.Collections/Delete',
                request_serializer=collections__pb2.DeleteCollection.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )
        self.UpdateAliases = channel.unary_unary(
                '/qdrant.Collections/UpdateAliases',
                request_serializer=collections__pb2.ChangeAliases.SerializeToString,
                response_deserializer=collections__pb2.CollectionOperationResponse.FromString,
                )
        self.ListCollectionAliases = channel.unary_unary(
                '/qdrant.Collections/ListCollectionAliases',
                request_serializer=collections__pb2.ListCollectionAliasesRequest.SerializeToString,
                response_deserializer=collections__pb2.ListAliasesResponse.FromString,
                )
        self.ListAliases = channel.unary_unary(
                '/qdrant.Collections/ListAliases',
                request_serializer=collections__pb2.ListAliasesRequest.SerializeToString,
                response_deserializer=collections__pb2.ListAliasesResponse.FromString,
                )
        self.CollectionClusterInfo = channel.unary_unary(
                '/qdrant.Collections/CollectionClusterInfo',
                request_serializer=collections__pb2.CollectionClusterInfoRequest.SerializeToString,
                response_deserializer=collections__pb2.CollectionClusterInfoResponse.FromString,
                )
        self.CollectionExists = channel.unary_unary(
                '/qdrant.Collections/CollectionExists',
                request_serializer=collections__pb2.CollectionExistsRequest.SerializeToString,
                response_deserializer=collections__pb2.CollectionExistsResponse.FromString,
                )
        self.UpdateCollectionClusterSetup = channel.unary_unary(
                '/qdrant.Collections/UpdateCollectionClusterSetup',
                request_serializer=collections__pb2.UpdateCollectionClusterSetupRequest.SerializeToString,
                response_deserializer=collections__pb2.UpdateCollectionClusterSetupResponse.FromString,
                )
        self.CreateShardKey = channel.unary_unary(
                '/qdrant.Collections/CreateShardKey',
                request_serializer=collections__pb2.CreateShardKeyRequest.SerializeToString,
                response_deserializer=collections__pb2.CreateShardKeyResponse.FromString,
                )
        self.DeleteShardKey = channel.unary_unary(
                '/qdrant.Collections/DeleteShardKey',
                request_serializer=collections__pb2.DeleteShardKeyRequest.SerializeToString,
                response_deserializer=collections__pb2.DeleteShardKeyResponse.FromString,
                )


class CollectionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """
        Get detailed information about specified existing collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """
        Get list name of all existing collections
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """
        Create new collection with given parameters
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """
        Update parameters of the existing collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """
        Drop collection and all associated data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAliases(self, request, context):
        """
        Update Aliases of the existing collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCollectionAliases(self, request, context):
        """
        Get list of all aliases for a collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAliases(self, request, context):
        """
        Get list of all aliases for all existing collections
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CollectionClusterInfo(self, request, context):
        """
        Get cluster information for a collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CollectionExists(self, request, context):
        """
        Check the existence of a collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCollectionClusterSetup(self, request, context):
        """
        Update cluster setup for a collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateShardKey(self, request, context):
        """
        Create shard key
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteShardKey(self, request, context):
        """
        Delete shard key
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollectionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=collections__pb2.GetCollectionInfoRequest.FromString,
                    response_serializer=collections__pb2.GetCollectionInfoResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=collections__pb2.ListCollectionsRequest.FromString,
                    response_serializer=collections__pb2.ListCollectionsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=collections__pb2.CreateCollection.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=collections__pb2.UpdateCollection.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=collections__pb2.DeleteCollection.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
            'UpdateAliases': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAliases,
                    request_deserializer=collections__pb2.ChangeAliases.FromString,
                    response_serializer=collections__pb2.CollectionOperationResponse.SerializeToString,
            ),
            'ListCollectionAliases': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCollectionAliases,
                    request_deserializer=collections__pb2.ListCollectionAliasesRequest.FromString,
                    response_serializer=collections__pb2.ListAliasesResponse.SerializeToString,
            ),
            'ListAliases': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAliases,
                    request_deserializer=collections__pb2.ListAliasesRequest.FromString,
                    response_serializer=collections__pb2.ListAliasesResponse.SerializeToString,
            ),
            'CollectionClusterInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.CollectionClusterInfo,
                    request_deserializer=collections__pb2.CollectionClusterInfoRequest.FromString,
                    response_serializer=collections__pb2.CollectionClusterInfoResponse.SerializeToString,
            ),
            'CollectionExists': grpc.unary_unary_rpc_method_handler(
                    servicer.CollectionExists,
                    request_deserializer=collections__pb2.CollectionExistsRequest.FromString,
                    response_serializer=collections__pb2.CollectionExistsResponse.SerializeToString,
            ),
            'UpdateCollectionClusterSetup': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCollectionClusterSetup,
                    request_deserializer=collections__pb2.UpdateCollectionClusterSetupRequest.FromString,
                    response_serializer=collections__pb2.UpdateCollectionClusterSetupResponse.SerializeToString,
            ),
            'CreateShardKey': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateShardKey,
                    request_deserializer=collections__pb2.CreateShardKeyRequest.FromString,
                    response_serializer=collections__pb2.CreateShardKeyResponse.SerializeToString,
            ),
            'DeleteShardKey': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteShardKey,
                    request_deserializer=collections__pb2.DeleteShardKeyRequest.FromString,
                    response_serializer=collections__pb2.DeleteShardKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'qdrant.Collections', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Collections(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Get',
            collections__pb2.GetCollectionInfoRequest.SerializeToString,
            collections__pb2.GetCollectionInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/List',
            collections__pb2.ListCollectionsRequest.SerializeToString,
            collections__pb2.ListCollectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Create',
            collections__pb2.CreateCollection.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Update',
            collections__pb2.UpdateCollection.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/Delete',
            collections__pb2.DeleteCollection.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAliases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/UpdateAliases',
            collections__pb2.ChangeAliases.SerializeToString,
            collections__pb2.CollectionOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCollectionAliases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/ListCollectionAliases',
            collections__pb2.ListCollectionAliasesRequest.SerializeToString,
            collections__pb2.ListAliasesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAliases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/ListAliases',
            collections__pb2.ListAliasesRequest.SerializeToString,
            collections__pb2.ListAliasesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CollectionClusterInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/CollectionClusterInfo',
            collections__pb2.CollectionClusterInfoRequest.SerializeToString,
            collections__pb2.CollectionClusterInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CollectionExists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/CollectionExists',
            collections__pb2.CollectionExistsRequest.SerializeToString,
            collections__pb2.CollectionExistsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCollectionClusterSetup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/UpdateCollectionClusterSetup',
            collections__pb2.UpdateCollectionClusterSetupRequest.SerializeToString,
            collections__pb2.UpdateCollectionClusterSetupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateShardKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/CreateShardKey',
            collections__pb2.CreateShardKeyRequest.SerializeToString,
            collections__pb2.CreateShardKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteShardKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/qdrant.Collections/DeleteShardKey',
            collections__pb2.DeleteShardKeyRequest.SerializeToString,
            collections__pb2.DeleteShardKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)