from ..common import ServiceObject
from ...models import ParticipantModel
from ...repositories import ParticipantRepo
import poro

class ParticipantService(ServiceObject):

    _repo_type = ParticipantRepo

    def add(self, match:poro.Match):
        _participants = self._new(match)

        for _p in _participants:
            self._insert(_p)

    def _new(self, match:poro.Match) -> list[ParticipantModel]:
        _participants = [_p.to_dict() for _p in match.participants]
        participants = []

        for _p in _participants:
            _participant = self.__repo__.zeros
            key = _p["participant_id"]
            _participant["key"] = key
            _participant["id"] = match.id + "0"*(2-len(str(key))) + str(key)
            _participant["team_key"] = _p["team_key"]
            _participant["match_id"] = match.id

            for k in _p.keys():
                _participant[k] = _p[k]
            
            participant = self.__repo__.new(**_participant)
            print(participant.id)
            participants.append(participant)
        
        return participants
    
    def get_match_ids(self, puuid:str, start:int=None, count:int=None) -> list[str]:
        if start==None:
            _match_ids = self.__repo__.create_query.find(puuid=puuid).select(["match_id"]).all()
        else:
            _match_ids = self.__repo__.create_query.find(puuid=puuid).select(["match_id"]).slice(start, count).all()
        return [m_id[0] for m_id in _match_ids]
    
    def get_participants(self, match_id:str) -> list[ParticipantModel]:
        return self.__repo__.create_query.find(match_id=match_id).all()