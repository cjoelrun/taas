from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from taas.database import Model, db


class TestRun(Model):
    id = db.Column(db.Integer, primary_key=True)
    test_case_id = db.Column(db.ForeignKey("test_case.id"))
    message = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    task_id = db.Column(db.String)
    # TODO: Constrain
    status = db.Column(db.String)
    runtime_data = db.Column(JSONB)

    parameter_id = db.Column(db.Integer, db.ForeignKey('parameter.id'))

    execution_runs = relationship("ExecutionRun", backref='TestRun')
