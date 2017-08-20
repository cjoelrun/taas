from sqlalchemy.orm import relationship

from taas.database import Model, db


class TestCase(Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    expected_success = db.Column(db.Boolean, default=True)

    parameter_group_id = db.Column(db.Integer, db.ForeignKey('parameter_group.id'))

    test_suite_id = db.Column(db.Integer, db.ForeignKey('test_suite.id'))

    test_runs = db.relationship("TestRun", backref='test_case', lazy='dynamic')
    steps = db.relationship("Step", backref='test_cases', lazy='dynamic')
