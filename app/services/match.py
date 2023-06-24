from ..repositories import MatchRepo, TeamRepo, ParticipantRepo
from ..models import MatchModel
import poro

class MatchSvc:
    __match_repo__ = MatchRepo()
    __team_repo__ = TeamRepo()
    __participant_repo__ = ParticipantRepo()

    def get_match(self, id) -> MatchModel:
        match = self.__match_repo__.get(id)
        match = match.serialize()
        return match
    
    def exists_match(self, id):
        return self.__match_repo__.exists(id)
    
    def add_match(self, match):
        print("add match")
        self._add_match(match)
        self._add_teams(match)
    
    def _add_match(self, match):
        _match = self.__match_repo__.new(**match)
        return self.__match_repo__.insert(_match)
    
    def get_all_match_ids(self):
        return self.__match_repo__.all_ids()
    
    def _add_teams(self, match):
        participants = match["participants"]
        match_id = match["id"]
        
        for i in range(2):
            _team = self.__team_repo__.zeros
            _team["key"] = str(100+(100*i))
            _team["id"] = match["id"] + _team["key"]
            _team["win"] = participants[5*i]["win"]
            _team["match_id"] = match_id
            for _p in participants[5*i:5*i+5]:
                for k, v in _team.items():
                    if type(v)==bool:
                        if _p[k]==True:
                            _team[k] = True
                    elif type(v)==int:
                        _team[k] += _p[k]
                
                self._add_participant(match_id, _p)
            
            team = self.__team_repo__.new(**_team)
            self.__team_repo__.insert(team)
    
    def _add_participant(self, match_id, p):
        _p = self.__participant_repo__.zeros
        p["key"] = p["participant_id"]
        p["id"] = match_id + "0"*(2-len(str(p["key"]))) + str(p["key"])
        p["team_key"] = str(p["team_key"])
        p["match_id"] = match_id
        for k in _p.keys():
            _p[k] = p[k]
        p = self.__participant_repo__.new(**_p)
        self.__participant_repo__.insert(p)
    
    def get_match_ids(self, puuid, start, count):
        query = self.__participant_repo__._find(puuid=puuid)
        query = self.__participant_repo__._slice(query, start, count)
        query = self.__participant_repo__._select(query, ["match_id"])
        ids = [p[0] for p in self.__participant_repo__._all(query)]
        return ids

    def get_teams(self, match_id):
        query = self.__team_repo__._find(match_id=match_id)
        teams = self.__team_repo__._all(query)
        teams = {team.key:team.serialize() for team in teams}
        return teams
    
    def get_participants(self, match_id):
        query = self.__participant_repo__._find(match_id=match_id)
        participants = self.__participant_repo__._all(query)
        participants = {participant.key:participant.serialize() for participant in participants}
        return participants