from ..common import RepoObject
from ...models import MatchModel, TeamModel, ParticipantModel

class MatchRepo(RepoObject):
    __model__ = MatchModel

class TeamRepo(RepoObject):
    __model__ = TeamModel

class ParticipantRepo(RepoObject):
    __model__ = ParticipantModel

    def get_match_ids(self, puuid:str, start:int=None, count:int=None):
        self.find(puuid=puuid).all()



        query = self.query
        query = self.find(query, puuid=puuid)
        query = self.select(query, ["match_id"])
        match_ids = []
        if start==None: # get all match by puuid
            [match_ids.append(p[0]) for p in self.all(query)]
        else: # get n match by puuid
            query = self.slice(query, start, count)
            [match_ids.append(p[0]) for p in self.all(query)]
        
        return match_ids