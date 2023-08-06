from ..common import ServiceObject
from ...models import PerkiconModel
from ...repositories import PerkiconRepo
import poro

class PerkiconService(ServiceObject):

    _repo_type = PerkiconRepo
    
    def add(self, perkicons):
        _perkicons = self._new(perkicons)
        
        for _p in _perkicons:
            self._insert(_p)

    def _new(self, perkicons:poro.PerkIcons) -> list[PerkiconModel]:
        _perkicons:list[PerkiconModel] = []
        
        for _p in perkicons.icons.values():
            _p["key"] = str(_p["id"])
            _p["id"] = "PJ" + perkicons.version_id + "0"*(4-len(_p["key"])) + _p["key"]
            _p["version_id"] = perkicons.version_id
            _p["path"] = f"/img/perkicon/{_p['key']}"
            _perkicon = self.__repo__.new(**_p)
            _perkicons.append(_perkicon)
        
        return _perkicons