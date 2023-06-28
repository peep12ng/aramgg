from ..common import ServiceObject
from ...models import SpellModel
from ...repositories import SpellRepo
import poro

class SpellService(ServiceObject):

    _repo_type = SpellRepo

    def add(self, version:str):
        spells = poro.Spells(version)
        _spells = self._new(spells)
        
        for _s in _spells:
            self._insert(_s)
    
    def _new(self, spells:poro.Spells) -> list[SpellModel]:
        _spells:list[SpellModel] = []

        for _s in spells.spells.values():
            _s["version_id"] = spells.version_id
            _s["id"] = "S" + spells.version_id + "0"*(4-len(_s["key"])) + _s["key"]
            spell = self.__repo__.new(**_s)
            _spells.append(spell)

        return _spells