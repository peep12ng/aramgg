from ...extensions import db
from sqlalchemy.dialects.mysql import MEDIUMBLOB

class PerkiconModel(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    key = db.Column(db.VARCHAR(10))
    binary = db.Column(MEDIUMBLOB)
    path = db.Column(db.VARCHAR(30))