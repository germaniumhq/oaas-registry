import collections
import uuid
from typing import Dict, Iterable, Set

from oaas_registry.registry import Registry
from oaas_registry.service_definition import ServiceDefinition


class RegistryMemory(Registry):
    def __init__(self) -> None:
        self._services: Dict[str, Set[ServiceDefinition]] = collections.defaultdict(set)

    def register_service(self, *, namespace: str = "default", name: str, version: str = "1", tags: Dict[str, str],
                         locations: Iterable[str]) -> ServiceDefinition:

        sd_tags = dict(tags)
        sd_tags["_instance_id"] = str(uuid.uuid4())

        sd = ServiceDefinition(
            namespace=namespace,
            name=name,
            version=version,
            tags=sd_tags,
            locations=locations,
        )

        _id = f"{namespace}:{name}:{version}"
        self._services[_id].add(sd)

        for tag_key, tag_value in sd_tags.items():
            self._services[f"{tag_key}={tag_value}"].add(sd)

        return sd

    def resolve_service(self, *, namespace: str = "default", name: str, version: str = "1", tags: Dict[str, str]) -> Iterable[ServiceDefinition]:
        _id = f"{namespace}:{name}:{version}"
        # we need a copy, because we'll filter them out inplace
        current_services = set(self._services[_id])

        for tag_key, tag_value in tags.items():
            current_services.intersection_update(self._services[f"{tag_key}={tag_value}"])

        return current_services

    def unregister_service(self, *, instance_id: str) -> bool:
        sd_set = self._services[f"_instance_id={instance_id}"]

        if not sd_set:
            return False

        sd = sd_set.__iter__().__next__()

        _id = f"{sd.namespace}:{sd.name}:{sd.version}"
        self._services[_id].remove(sd)

        for tag_key, tag_value in sd.tags.items():
            self._services[f"{tag_key}={tag_value}"].remove(sd)

        del self._services[f"_instance_id={instance_id}"]
