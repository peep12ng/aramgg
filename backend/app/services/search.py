from .riotapi import RiotAPIService

class SearchService:

    _riotapi_svc = RiotAPIService()

    def search(self, region:str, name:str, start:int, count:int):
        summoner = self._riotapi_svc.get_summoner(region=region, name=name)
        match_ids = self._riotapi_svc.get_match_ids(summoner["puuid"], start, count)

        result = {
            "summoner":summoner,
            "history":
            {m_id:
                {
                    "match":self._riotapi_svc.get_match(m_id),
                    "teams":self._riotapi_svc.get_teams(m_id),
                    "participants":self._riotapi_svc.get_participants(m_id)
                }
                for m_id in match_ids}
        }

        return result