from ..common import ServiceObject
from ...models import ItemModel
from ...repositories import ItemRepo
import poro

class ItemService(ServiceObject):

    _repo_type = ItemRepo
    
    def add(self, items):
        _items = self._new(items)
        
        for _i in _items:
            self._insert(_i)

    def _new(self, items:poro.Items) -> list[ItemModel]:
        _items:list[ItemModel] = []
        
        for k, _i in items.items.items():
            if _i["name"].startswith("<")==False:
                _i["id"] = "I" + items.version_id + "0"*(4-len(k)) + k
                _i["key"] = k
                _i["version_id"] = items.version_id
                _item = self.__repo__.new(**_i)
                _items.append(_item)
        
        return _items