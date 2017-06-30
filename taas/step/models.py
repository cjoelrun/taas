from sqlalchemy.orm import relationship

from taas.database import Model, db


class Step(Model):
    __tablename__ = 'step'

    test_case_id = db.Column(db.Integer, db.ForeignKey('test_case.id'), primary_key=True)
    execution_id = db.Column(db.Integer, db.ForeignKey('execution.id'), primary_key=True)
    order = db.Column(db.Integer)
    execution = relationship("Execution")