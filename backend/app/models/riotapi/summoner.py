from ...extensions import db
import datetime

now = datetime.datetime.now()

class SummonerModel(db.Model):

    update_only = {"name", "level" ,"icon_id"}
    serialize_rules = {"update_at"}

    puuid = db.Column(db.VARCHAR(100), primary_key=True)
    region = db.Column(db.VARCHAR(10))
    name = db.Column(db.VARCHAR(50))
    level = db.Column(db.Integer)
    icon_id = db.Column(db.VARCHAR(20))
    update_at = db.Column(db.DateTime, default=now, onupdate=now)