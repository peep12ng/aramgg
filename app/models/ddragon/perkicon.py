from ...extensions import db
from sqlalchemy.dialects.mysql import MEDIUMBLOB

class PerkiconModel(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    key = db.Column(db.VARCHAR(10))
    binary = db.Column(MEDIUMBLOB)
    path = db.Column(db.VARCHAR(30))

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.version_id = kwargs.get("version_id", None)
        self.key = kwargs.get("key", None)
        self.binary = kwargs.get("binary", bytes)
        self.path = f"/img/perkicon/{self.key}"