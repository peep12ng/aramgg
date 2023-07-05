from ...extensions import db

class StyleModel(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    key = db.Column(db.VARCHAR(5))
    name = db.Column(db.VARCHAR(20))
    icon = db.Column(db.VARCHAR(100))

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.version_id = kwargs.get("version_id", None)
        self.key = kwargs.get("key", None)
        self.name = kwargs.get("name", None)
        self.icon = f"/img/icon/perk/style/{self.key}"

class RuneModel(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    key = db.Column(db.VARCHAR(5))
    name = db.Column(db.TEXT)
    shortDesc = db.Column(db.TEXT)
    longDesc = db.Column(db.TEXT)
    icon = db.Column(db.VARCHAR(100))

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.version_id = kwargs.get("version_id", None)
        self.key = kwargs.get("key", None)
        self.name = kwargs.get("name", None)
        self.shortDesc = kwargs.get("shortDesc", None)
        self.longDesc = kwargs.get("longDesc", None)
        self.icon = f"/img/icon/perk/rune/{self.key}"

class ShardModel(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    key = db.Column(db.VARCHAR(5))
    name = db.Column(db.VARCHAR(20))
    shortDesc = db.Column(db.TEXT)
    longDesc = db.Column(db.TEXT)
    icon = db.Column(db.VARCHAR(100))

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.version_id = kwargs.get("version_id", None)
        self.key = kwargs.get("key", None)
        self.name = kwargs.get("name", None)
        self.shortDesc = kwargs.get("shortDesc", None)
        self.longDesc = kwargs.get("longDesc", None)
        self.icon = f"/img/icon/perk/shard/{self.key}"