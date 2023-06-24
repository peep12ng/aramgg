from ...extensions import db
import datetime

now = datetime.datetime.now()

class SummonerModel(db.Model):
    puuid = db.Column(db.VARCHAR(100), primary_key=True)
    region = db.Column(db.VARCHAR(10))
    name = db.Column(db.VARCHAR(50))
    level = db.Column(db.Integer)
    icon_id = db.Column(db.VARCHAR(20))
    update_at = db.Column(db.DateTime, default=now, onupdate=now)

    def __init__(self, **kwargs):
        self.puuid = kwargs.get("puuid", None)
        self.region = kwargs.get("region", None)
        self.name = kwargs.get("name", None)
        self.level = kwargs.get("level", None)
        self.icon_id = kwargs.get("icon_id", None)
    
    def serialize(self):
        return {
            "puuid":self.puuid,
            "region":self.region,
            "name":self.name,
            "level":self.level,
            "icon_id":self.icon_id
        }