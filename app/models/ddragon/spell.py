from ...extensions import db

class SpellModel(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    key = db.Column(db.VARCHAR(5))
    name = db.Column(db.VARCHAR(20))
    image = db.Column(db.JSON)

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.version_id = kwargs.get("version_id", None)
        self.key = kwargs.get("key", None)
        self.name = kwargs.get("name", None)
        self.image = kwargs.get("image", dict)