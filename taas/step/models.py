from sqlalchemy.orm import relationship

from taas.database import Model, db


class Step(Model):
    id = db.Column(db.Integer, primary_key=True)
    test_case_id = db.Column(db.Integer, db.ForeignKey('test_case.id'))
    execution_id = db.Column(db.Integer, db.ForeignKey('execution.id'))
    order = db.Column(db.Integer)

    execution_runs = db.relationship("ExecutionRun", backref="step")

    def serialize(self):
        return {
            'id': self.id,
            'test_case_id': self.test_case_id,
            'execution_id': self.execution_id,
            'order': self.order,
            'execution_runs': self.serialize_execution_runs()
        }

    def serialize_execution_runs(self):
        return [item.serialize() for item in self.execution_runs]
