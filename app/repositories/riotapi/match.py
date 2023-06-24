from ..common import RepoObject
from ...models import MatchModel, TeamModel, ParticipantModel

class MatchRepo(RepoObject):
    __model__ = MatchModel

class TeamRepo(RepoObject):
    __model__ = TeamModel

class ParticipantRepo(RepoObject):
    __model__ = ParticipantModel