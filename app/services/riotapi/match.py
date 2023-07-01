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
    
    def sort_match_ids(self, match_ids:list[str]) -> list[str]:
        _match_ids = self.__repo__.create_query.select(["id"]).filter_in("id", match_ids).order_by(["creation"]).all()
        return [m_id[0] for m_id in _match_ids]