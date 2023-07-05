from ...extensions import db

class ItemModel(db.Model):
    id = db.Column(db.VARCHAR(20), primary_key=True)
    version_id = db.Column(db.VARCHAR(10), db.ForeignKey("version_model.id"))
    key = db.Column(db.VARCHAR(5))
    name = db.Column(db.VARCHAR(20))
    image = db.Column(db.JSON)