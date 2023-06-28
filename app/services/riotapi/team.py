from ..common import ServiceObject
from ...models import TeamModel
from ...repositories import TeamRepo
import poro

class TeamService(ServiceObject):
    
    _repo_type = TeamRepo

    def add(self, match:poro.Match):
        _teams = self._new(match)
        for _t in _teams:
            self._insert(_t)

    def _new(self, match:poro.Match) -> list[TeamModel]:
        print(len(match.participants))
        participants = [_p.to_dict() for _p in match.participants]
        print(len(participants))
        match_id = match.id

        teams = []

        for i in range(2):
            _team = self.__repo__.zeros
            _team["key"] = str(100+(100*i))
            _team["id"] = match_id + _team["key"]
            _team["win"] = participants[5*i]["win"]
            _team["match_id"] = match_id
            for _p in participants[5*i:5*i+5]:
                print(len(match.participants))
                for k, v in _team.items():
                    if type(v)==bool:
                        if _p[k]==True:
                            _team[k] = True
                    elif type(v)==int:
                        _team[k] += _p[k]
            
            team = self.__repo__.new(**_team)
            teams.append(team)
        
        return teams
    
    def get_teams(self, match_id:str) -> list[TeamModel]:
        return self.__repo__.create_query.find(match_id=match_id).all()