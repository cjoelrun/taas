from sqlalchemy.orm import relationship

from taas.database import Model, db

test_parameters = db.Table('test_parameters',
    db.Column('test_case_id', db.Integer, db.ForeignKey('test_case.id')),
    db.Column('parameter_id', db.Integer, db.ForeignKey('parameter.id'))
)


class TestCase(Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    expected_success = db.Column(db.Boolean, default=True)

    test_suite_id = db.Column(db.Integer, db.ForeignKey('test_suite.id'))

    test_runs = db.relationship("TestRun", backref='test_case', lazy='dynamic')
    steps = db.relationship("Step", backref='test_cases', lazy='dynamic')
    parameters = db.relationship("Parameter", secondary=test_parameters, backref=db.backref('test_cases', lazy='dynamic'))
