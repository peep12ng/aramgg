from ..common import ServiceObject
from ...models import ChampionModel
from ...repositories import ChampionRepo
import poro

class ChampionService(ServiceObject):

    _repo_type = ChampionRepo
    
    def add(self, version:str):
        champions = poro.Champions(version)
        _champions = self._new(champions)
        
        for _c in _champions:
            self._insert(_c)

    def _new(self, champions:poro.Champions) -> list[ChampionModel]:
        _champions:list[ChampionModel] = []
        
        for _c in champions.champions.values():
            _c["id"] = "C" + champions.version_id + "0"*(4-len(_c["key"])) + _c["key"]
            _c["version_id"] = champions.version_id
            _champion = self.__repo__.new(**_c)
            _champions.append(_champion)
        
        return _champions