
from taas.database import Model, db


class Step(Model):
    id = db.Column(db.Integer, primary_key=True)
    test_case_id = db.Column(db.Integer, db.ForeignKey('test_case.id'))
    execution_id = db.Column(db.Integer, db.ForeignKey('execution.id'))
    order = db.Column(db.Integer)

    execution_runs = db.relationship("ExecutionRun", backref="step")
