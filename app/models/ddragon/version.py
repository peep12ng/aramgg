from ...extensions import db

class VersionModel(db.Model):
    id = db.Column(db.VARCHAR(10), primary_key=True)
    version = db.Column(db.VARCHAR(10))
    season = db.Column(db.Integer)
    count = db.Column(db.Integer)

    _match = db.relationship('MatchModel', backref='version_model')
    _champion = db.relationship('ChampionModel', backref='version_model')
    _item = db.relationship('ItemModel', backref='version_model')
    _spell = db.relationship('SpellModel', backref='version_model')
    _style = db.relationship('StyleModel', backref='version_model')
    _rune = db.relationship('RuneModel', backref='version_model')
    _shard = db.relationship('ShardModel', backref='version_model')
    _sprite = db.relationship('SpriteModel', backref='version_model')
    _profileicon = db.relationship('ProfileiconModel', backref='version_model')
    _perkicon = db.relationship('PerkiconModel', backref='version_model')