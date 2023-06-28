from ..common import ServiceObject
from ...models import MatchModel
from ...repositories import MatchRepo
import poro

class MatchService(ServiceObject):

    _repo_type = MatchRepo
    
    def add(self, match:poro.Match) -> MatchModel:
        _match = self._new(match)
        self._insert(_match)

    def _new(self, match:poro.Match) -> MatchModel:
        return self.__repo__.new(**match.to_dict())