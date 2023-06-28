from ..common import ServiceObject
from ...models import SpriteModel
from ...repositories import SpriteRepo
import poro

class SpriteService(ServiceObject):

    _repo_type = SpriteRepo
    
    def add(self, version:str):
        sprites = poro.Sprites(version)
        _sprites = self._new(sprites)
        
        for _s in _sprites:
            self._insert(_s)

    def _new(self, sprites:poro.Sprites) -> list[SpriteModel]:
        _sprites:list[SpriteModel] = []
        
        key = 0
        for type in sprites.sprites.values():
            for v in type.values():
                _s = {}
                _s["id"] = "SP" + sprites.version_id + "0"*(3-len(str(key))) + str(key)
                _s["version_id"] = sprites.version_id
                _s["key"] = str(key)
                _s["binary"] = v
                _s["path"] = f"/img/sprite/{str(key)}"

                _sprite = self.__repo__.new(**_s)
                _sprites.append(_sprite)
                key += 1
        
        return _sprites