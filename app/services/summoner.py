from ..repositories import SummonerRepo
from ..models import SummonerModel
import poro

class SummonerSvc:
    __summoner_repo__ = SummonerRepo()

    def get_summoner(self, region:str, puuid:str=None, name:str=None):
        if puuid:
            return self.__summoner_repo__.first(region=region, puuid=puuid).serialize()
        else:
            return self.__summoner_repo__.first(region=region, name=name).serialize()
    
    def exists_summoner(self, puuid):
        return self.__summoner_repo__.exists(puuid)

    def update_summoner(self, summoner):
        _summoner = self.__summoner_repo__.new(**summoner)
        return self.__summoner_repo__.update(_summoner)
    
    def add_summoner(self, summoner):
        _summoner = self.__summoner_repo__.new(**summoner)
        return self.__summoner_repo__.insert(_summoner)