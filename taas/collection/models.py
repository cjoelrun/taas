from sqlalchemy.orm import relationship

from taas.database import Model, db


class Collection(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    test_cases = relationship("TestCase")
