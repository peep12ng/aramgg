from ..common import ServiceObject
from ...models import RuneModel
from ...repositories import RuneRepo
import poro

class RuneService(ServiceObject):

    _repo_type = RuneRepo

    def add(self, version:str):
        perks = poro.Perks(version)
        _runes = self._new(perks)
        
        for _r in _runes:
            self._insert(_r)
    
    def _new(self, perks:poro.Perks) -> list[RuneModel]:
        _runes:list[RuneModel] = []

        for _p in perks.perks:
            _p["version_id"] = perks.version_id
            _p["key"] = str(_p["id"])
            _p["id"] = "R" + perks.version_id + "0"*(4-len(_p["key"])) + _p["key"]
            if not _p["key"].startswith("5"):
                _rune = self.__repo__.new(**_p)
                _runes.append(_rune)
        
        return _runes