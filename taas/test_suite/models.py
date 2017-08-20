from taas.database import Model, db

test_cases = db.Table('test_suite_cases',
    db.Column('test_case_id', db.Integer, db.ForeignKey('test_case.id')),
    db.Column('test_suite_id', db.Integer, db.ForeignKey('test_suite.id'))
)


class TestSuite(Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)

    parameter_group_id = db.Column(db.Integer, db.ForeignKey('parameter_group.id'))

    test_cases = db.relationship("TestCase", secondary=test_cases, backref=db.backref('test_cases', lazy='dynamic'))

    test_suite_runs = db.relationship("TestSuiteRun", backref='test_suite', lazy='dynamic')
