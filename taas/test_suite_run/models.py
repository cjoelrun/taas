from sqlalchemy.dialects.postgresql import JSONB
from taas.database import Model, db

test_case_runs = db.Table('test_suite_case_runs',
    db.Column('test_case_run_id', db.Integer, db.ForeignKey('test_run.id')),
    db.Column('test_suite_run_id', db.Integer, db.ForeignKey('test_suite_run.id'))
)


class TestSuiteRun(Model):
    id = db.Column(db.Integer, primary_key=True)
    test_suite_id = db.Column(db.ForeignKey("test_suite.id"))
    message = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    # TODO: Constrain
    status = db.Column(db.String)
    runtime_data = db.Column(JSONB)

    test_case_runs = db.relationship("TestRun", secondary=test_case_runs, backref=db.backref('test_runs', lazy='dynamic'))
