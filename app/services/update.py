from .summoner import SummonerSvc
from .match import MatchSvc
from .ddragon import DdragonSvc
import poro

from ..utils import version_to_id, match_version_to_version

class UpdateSvc:
    __summoner_svc__ = SummonerSvc()
    __match_svc__ = MatchSvc()
    __ddragon_svc__ = DdragonSvc()

    def update(self, region, puuid:str=None, name:str=None):
        summoner = poro.Summoner(region, puuid, name)
        self.update_summoner(summoner)

        history = summoner.match_history(0, 5).match_ids
        all_ids = self.__match_svc__.get_all_match_ids()

        match_ids = list(set(history) - set(all_ids))

        for m_id in match_ids:
            _match = poro.Match(region, id=m_id)
            version = match_version_to_version(_match.version)

            if self.__ddragon_svc__.exists_ddragon(version)==False:
                self.__ddragon_svc__.add_ddragon(version)
            
            if self.__match_svc__.exists_match(_match.id)==False:
                match = _match.to_dict()
                match["version_id"] = version_to_id(version)
                self.__match_svc__.add_match(match)

    def update_summoner(self, summoner:poro.Summoner):
        if self.__summoner_svc__.exists_summoner(summoner.puuid):
            return self.__summoner_svc__.update_summoner(summoner.to_dict())
        else:
            return self.__summoner_svc__.add_summoner(summoner.to_dict())