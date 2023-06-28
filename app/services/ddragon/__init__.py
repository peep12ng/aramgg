from .version import VersionService
from .champion import ChampionService
from .item import ItemService
from .rune import RuneService
from .shard import ShardService
from .style import StyleService
from .spell import SpellService
from .sprite import SpriteService
from .profileicon import ProfileiconService
from .perkicon import PerkiconService

class DdragonService:

    _version_svc = VersionService()
    _champion_svc = ChampionService()
    _item_svc = ItemService()
    _rune_svc = RuneService()
    _shard_svc = ShardService()
    _style_svc = StyleService()
    _spell_svc = SpellService()
    _sprite_svc = SpriteService()
    _profileicon_svc = ProfileiconService()
    _perkicon_svc = PerkiconService()

    def update_ddragon(self, version:str):
        if self._version_svc.exists(version)==False:
            print(f"Start Update Ddragon ver:{version}")
            self._version_svc.add(version)
            self._champion_svc.add(version)
            self._item_svc.add(version)
            self._rune_svc.add(version)
            self._shard_svc.add(version)
            self._style_svc.add(version)
            self._sprite_svc.add(version)
            # self._profileicon_svc.add(version)
            # self._perkicon_svc.add(version)
        
            print(f"Complete Update Ddragon ver:{version}")