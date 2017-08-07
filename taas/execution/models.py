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

    def serialize(self):
        return {
            'id': self.id,
            'description': self.description,
            'type': self.type,
            'strategy': self.strategy,
            'data': self.data,
            'steps': self.serialize_steps()
        }

    def serialize_steps(self):
        return [item.serialize() for item in self.steps]

    def update_fields(self, json):
        self.data = json.get('data', None)
        self.description = json.get('description', None)
        self.strategy = json.get('strategy', None)
        self.type = json.get('type', None)

