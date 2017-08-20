from sqlalchemy.orm import relationship
from taas.database import Model, db


class ParameterGroup(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    parameters = relationship("Parameter", backref='ParameterGroup')
