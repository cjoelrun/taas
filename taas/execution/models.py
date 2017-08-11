from sqlalchemy.dialects.postgresql import JSONB

from taas.database import Model, db


class Execution(Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    # TODO: Constrain
    type = db.Column(db.String)
    strategy = db.Column(db.String)
    data = db.Column(JSONB)

    steps = db.relationship("Step", backref="execution")
