import oaas

from oaas_registry.rpc.oaas_registry_pb2_grpc import OaasRegistryServicer


@oaas.service("oaas-registry")
class OaasGrpcRegistry(OaasRegistryServicer):
    pass
