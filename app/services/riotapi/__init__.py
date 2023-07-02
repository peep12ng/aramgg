from ...models import SummonerModel, MatchModel, TeamModel, ParticipantModel
from .summoner import SummonerService
from .match import MatchService
from .team import TeamService
from .participant import ParticipantService

from ...extensions import aramgg_poro as poro

class RiotAPIService:
        
    _summoner_svc = SummonerService()
    _match_svc = MatchService()
    _team_svc = TeamService()
    _participant_svc = ParticipantService()

    def update_summoner(self, summoner:poro.Summoner) -> SummonerModel:
        return self._summoner_svc.update(summoner)

    def get_history(self, region:str, puuid:str, start:int=None, count:int=None) -> poro.MatchHistory:
        return poro.MatchHistory(continent=poro.Region(region.upper()).continent, puuid=puuid, start=start, count=count)
    
    def drop_duplicate_match_ids(self, match_ids:list[str], puuid:str) -> list[str]:
        _match_ids = self._participant_svc.get_match_ids(puuid)

        return list(set(match_ids) - set(_match_ids))
    
    def add_match(self, match:poro.Match):
        self._match_svc.add(match)
        self._team_svc.add(match)
        self._participant_svc.add(match)

        print(f"Add Match id {match.id}")
    
    def get_summoner(self, region:str, name:str) -> dict:
        return self._summoner_svc.get(region=region, name=name).serialize()
    
    def get_match_ids(self, puuid:str, start:int, count:int) -> list[str]:
        _match_ids = self._participant_svc.get_match_ids(puuid, start, count)
        return self._match_svc.sort_match_ids(_match_ids)

    def get_match(self, match_id:str) -> dict:
        return self._match_svc._read(match_id).serialize()
    
    def get_teams(self, match_id:str) -> dict:
        return {team.key:team.serialize() for team in self._team_svc.get_teams(match_id=match_id)}
    
    def get_participants(self, match_id:str) -> dict:
        return {p.key:p.serialize() for p in self._participant_svc.get_participants(match_id=match_id)}