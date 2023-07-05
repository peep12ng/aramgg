from ..repositories.common import RepoObject
from ..extensions import ModelObject
from abc import abstractmethod, ABCMeta

class ServiceObject(metaclass=ABCMeta):
    
    _repo_type:type[RepoObject] = None

    def __init__(self):
        self.__repo__ = self._repo_type()

    @abstractmethod
    def _new(self):
        pass

    def _read(self, id:str) -> ModelObject:
        return self.__repo__.get(id)

    def _insert(self, obj:ModelObject) -> ModelObject:
        return self.__repo__.insert(obj)
    
    def _update(self, obj:ModelObject) -> ModelObject:
        return self.__repo__.update(obj)
    
    def _delete(self, id:str):
        self.__repo__.delete(id)

    def _exists(self, id:str) -> bool:
        return self.__repo__.exists(id)