from ..common import ServiceObject
from ...models import ProfileiconModel
from ...repositories import ProfileiconRepo
import poro

class ProfileiconService(ServiceObject):

    _repo_type = ProfileiconRepo
    
    def add(self, version:str):
        profileicons = poro.ProfileIcons(version)
        _profileicons = self._new(profileicons)
        
        for _p in _profileicons:
            self._insert(_p)

    def _new(self, profileicons:poro.ProfileIcons) -> list[ProfileiconModel]:
        _profileicons:list[ProfileiconModel] = []
        
        for _p in profileicons.profile_icons.values():
            _p["key"] = str(_p["id"])
            _p["id"] = "PI" + profileicons.version_id + "0"*(4-len(_p["key"])) + _p["key"]
            _p["version_id"] = profileicons.version_id
            _profileicon = self.__repo__.new(**_p)
            _profileicons.append(_profileicon)
        
        return _profileicons