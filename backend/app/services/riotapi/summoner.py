from ..common import ServiceObject
from ...models import SummonerModel
from ...repositories import SummonerRepo
import poro

class SummonerService(ServiceObject):

    _repo_type = SummonerRepo

    def update(self, summoner:poro.Summoner) -> SummonerModel:
        summoner = self._new(summoner)
        if self._exists(summoner.puuid):
            return self._update(summoner)
        else:
            return self._insert(summoner)
    
    def get(self, region:str, name:str):
        return self.__repo__.create_query.find(region=region, name=name).first()

    def _new(self, summoner:poro.Summoner) -> SummonerModel:
        return self.__repo__.new(**summoner.to_dict())