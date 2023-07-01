from .riotapi import RiotAPIService
from .ddragon import DdragonService
import poro

class UpdateService:

    _riotapi_svc = RiotAPIService()
    _ddragon_svc = DdragonService()

    def update(self, region:str, puuid:str=None, name:str=None, start:int=None, count:int=None):
        summoner = self.update_summoner(region, puuid, name)
        puuid = summoner.puuid

        history = poro.MatchHistory(poro.Region(region.upper()).continent, puuid, start, count)
        
        match_ids = self._riotapi_svc.drop_duplicate_match_ids(history.match_ids, puuid)

        for m_id in match_ids:
            match = poro.Match(region=region, id=m_id)
            self._ddragon_svc.update_ddragon(match.version)
            self._riotapi_svc.add_match(match)
    
    def update_summoner(self, region:str, puuid:str=None, name:str=None):
        summoner = poro.Summoner(region, puuid, name)
        return self._riotapi_svc.update_summoner(summoner)