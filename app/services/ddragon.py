from ..repositories import VersionRepo, ChampionRepo, ItemRepo, StyleRepo, RuneRepo, ShardRepo, SpellRepo, SpriteRepo, ProfileiconRepo
import poro
from ..utils import version_to_id

class DdragonSvc:
    __version_repo__ = VersionRepo()
    __champion_repo__ = ChampionRepo()
    __item_repo__ = ItemRepo()
    __style_repo__ = StyleRepo()
    __rune_repo__ = RuneRepo()
    __shard_repo__ = ShardRepo()
    __spell_repo__ = SpellRepo()
    __sprite_repo__ = SpriteRepo()
    __profileicon_repo__ = ProfileiconRepo()

    def exists_ddragon(self, version):
        return self.__version_repo__.exists(version_to_id(version))

    def add_ddragon(self, version):
        print("add ddragon")
        self._add_version(version)
        self._add_champions(version)
        self._add_items(version)
        self._add_perks(version)
        self._add_spells(version)
        self._add_sprites(version)
        self._add_profileicons(version)
    
    def _add_version(self, version):
        d = {
            "id":version_to_id(version),
            "version":version,
            "season":version.split(".")[0],
            "count":version.split(".")[1]
        }
        _version = self.__version_repo__.new(**d)
        self.__version_repo__.insert(_version)

    def _add_champions(self, version):
        champions = poro.Champions(version).champions
        version_id = version_to_id(version)

        for c in champions.values():
            c["id"] = "C" + version_id + "0"*(4-len(c["key"])) + c["key"]
            c["version_id"] = version_id
            champion = self.__champion_repo__.new(**c)
            self.__champion_repo__.insert(champion)
    
    def _add_items(self, version):
        items = poro.Items(version).items
        version_id = version_to_id(version)

        for k, i in items.items():
            if i["name"].startswith("<")==False:
                i["id"] = "I" + version_id + "0"*(4-len(k)) + k
                i["key"] = k
                i["version_id"] = version_id
                item = self.__item_repo__.new(**i)
                self.__item_repo__.insert(item)

    def _add_perks(self, version):
        _perks = poro.Perks(version) 
        perks = _perks.perks
        version_id = version_to_id(version)

        for _perk in perks:
            _perk["version_id"] = version_id
            _perk["key"] = str(_perk["id"])
            if _perk["key"].startswith("5"):
                self._add_shard(_perk)
            else:
                self._add_rune(_perk)
        
        styles = _perks.styles

        for _style in styles:
            _style["key"] = str(_style["id"])
            _style["id"] = "ST" + version_id + "0"*(4-len(_style["key"])) + _style["key"]
            _style["version_id"] = version_id
            style = self.__style_repo__.new(**_style)
            self.__style_repo__.insert(style)
    
    def _add_icon(self, version, d):
        _icon = {}
        _icon["version_id"] = version_to_id(version)
        _icon["key"] = d["id"]
        _icon["id"] = "IC" + _icon["version_id"] + "0"*(4-len(_icon["id"])) + _icon["id"]
    
    def _add_rune(self, rune):
        rune["id"] = "R" + rune["version_id"] + "0"*(4-len(rune["key"])) + rune["key"]
        _rune = rune
        rune = self.__rune_repo__.new(**_rune)
        self.__rune_repo__.insert(rune)
    
    def _add_shard(self, shard):
        shard["id"] = "SH" + shard["version_id"] + "0"*(4-len(shard["key"])) + shard["key"]
        _shard = shard
        shard = self.__shard_repo__.new(**_shard)
        self.__shard_repo__.insert(shard)
    
    def _add_spells(self, version):
        spells = poro.Spells(version).spells
        version_id = version_to_id(version)

        for s in spells.values():
            s["id"] = "S" + version_id + "0"*(4-len(s["key"])) + s["key"]
            s["version_id"] = version_id
            spell = self.__spell_repo__.new(**s)
            self.__spell_repo__.insert(spell)

    def _add_sprites(self, version):
        sprites = poro.Sprites(version).sprites
        version_id = version_to_id(version)

        key = 0
        for type in sprites.values():
            for v in type.values():
                _sprite = {}
                _sprite["id"] = "SP" + version_id + "0"*(3-len(str(key))) + str(key)
                _sprite["version_id"] = version_id
                _sprite["key"] = str(key)
                _sprite["binary"] = v

                sprite = self.__sprite_repo__.new(**_sprite)
                self.__sprite_repo__.insert(sprite)
                key = key + 1
    
    def _add_profileicons(self, version):
        profileicons = poro.ProfileIcons(version).profile_icons
        version_id = version_to_id(version)

        for _pi in profileicons.values():
            _pi["key"] = str(_pi["id"])
            _pi["id"] = "PI" + version_id + "0"*(4-len(_pi["key"])) + _pi["key"]
            _pi["version_id"] = version_id
            pi = self.__profileicon_repo__.new(**_pi)
            self.__profileicon_repo__.insert(pi)