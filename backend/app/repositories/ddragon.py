from .common import RepoObject
from ..models import VersionModel, ChampionModel, ItemModel, StyleModel, RuneModel, ShardModel, SpellModel, SpriteModel, ProfileiconModel, PerkiconModel

class VersionRepo(RepoObject):
    __model__ = VersionModel

class ChampionRepo(RepoObject):
    __model__ = ChampionModel

class ItemRepo(RepoObject):
    __model__ = ItemModel

class StyleRepo(RepoObject):
    __model__ = StyleModel

class RuneRepo(RepoObject):
    __model__ = RuneModel

class ShardRepo(RepoObject):
    __model__ = ShardModel

class SpellRepo(RepoObject):
    __model__ = SpellModel

class SpriteRepo(RepoObject):
    __model__ = SpriteModel

class ProfileiconRepo(RepoObject):
    __model__ = ProfileiconModel

class PerkiconRepo(RepoObject):
    __model__ = PerkiconModel