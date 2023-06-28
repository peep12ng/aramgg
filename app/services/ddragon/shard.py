from ..common import ServiceObject
from ...models import ShardModel
from ...repositories import ShardRepo
import poro

class ShardService(ServiceObject):

    _repo_type = ShardRepo

    def add(self, version:str):
        perks = poro.Perks(version)
        _shards = self._new(perks)
        
        for _s in _shards:
            self._insert(_s)
    
    def _new(self, perks:poro.Perks) -> list[ShardModel]:
        _shards:list[ShardModel] = []

        for _p in perks.perks:
            _p["version_id"] = perks.version_id
            _p["key"] = str(_p["id"])
            _p["id"] = "SH" + perks.version_id + "0"*(4-len(_p["key"])) + _p["key"]
            if _p["key"].startswith("5"):
                _shard = self.__repo__.new(**_p)
                _shards.append(_shard)
        
        return _shards