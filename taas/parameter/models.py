from sqlalchemy.dialects.postgresql import JSONB

from taas.database import Model, db


class Parameter(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # TODO: Constrain
    type = db.Column(db.String)
    data = db.Column(JSONB)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'data': self.data,
        }

    def update_fields(self, json):
        self.data = json.get('data', None)
        self.name = json.get('name', None)
        self.type = json.get('type', None)
