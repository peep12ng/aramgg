from ..common import ServiceObject
from ...models import VersionModel
from ...repositories import VersionRepo

from ...utils import version_to_id

class VersionService(ServiceObject):

    _repo_type = VersionRepo

    def exists(self, version:str) -> bool:
        return self._exists(self._new(version).id)
    
    def add(self, version:str):
        _version = self._new(version)
        self._insert(_version)

    def _new(self, version:str) -> VersionModel:
        _version = {
            "id":version_to_id(version),
            "version":version,
            "season":version.split(".")[0],
            "count":version.split(".")[1]
        }
        return self.__repo__.new(**_version)