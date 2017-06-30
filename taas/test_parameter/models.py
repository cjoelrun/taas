from sqlalchemy.orm import relationship

from taas.database import Model, db


class TestParameter(Model):
    __tablename__ = 'test_parameter'

    test_case_id = db.Column(db.Integer, primary_key=True)
    parameter_id = db.Column(db.Integer, primary_key=True)
    parameter = relationship("Parameter")




