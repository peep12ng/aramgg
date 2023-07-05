from ..common import RepoObject
from ...models import SummonerModel

class SummonerRepo(RepoObject):
    __model__ = SummonerModel
    __updates__ = ["name", "level" ,"icon_id"]