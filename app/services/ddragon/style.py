from ..common import ServiceObject
from ...models import StyleModel
from ...repositories import StyleRepo
import poro

class StyleService(ServiceObject):

    _repo_type = StyleRepo

    def add(self, perks):
        _styles = self._new(perks)
        
        for _s in _styles:
            self._insert(_s)
    
    def _new(self, perks:poro.Perks) -> list[StyleModel]:
        _styles:list[StyleModel] = []

        for _s in perks.styles:
            _s["version_id"] = perks.version_id
            _s["key"] = str(_s["id"])
            _s["id"] = "ST" + perks.version_id + "0"*(4-len(_s["key"])) + _s["key"]
            _style = self.__repo__.new(**_s)
            _styles.append(_style)
        
        return _styles