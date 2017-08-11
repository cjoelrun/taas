from sqlalchemy.dialects.postgresql import JSONB

from taas.database import Model, db


class Parameter(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # TODO: Constrain
    type = db.Column(db.String)
    data = db.Column(JSONB)
