from .summoner import SummonerSvc
from .match import MatchSvc

class SearchSvc:
    __summoner_svc__ = SummonerSvc()
    __match_svc__ = MatchSvc()

    def search(self, region, name):
        summoner = self.__summoner_svc__.get_summoner(region=region, name=name)

        match_ids = self.__match_svc__.get_match_ids(summoner['puuid'], 0, 3)

        result = {
            "summoner":summoner,
            "matches":{m_id:{"match":self.__match_svc__.get_match(m_id),
                             "teams":self.__match_svc__.get_teams(m_id),
                             "participants":self.__match_svc__.get_participants(m_id)} for m_id in match_ids}
        }

        return result