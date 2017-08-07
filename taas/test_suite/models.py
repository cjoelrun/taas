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

    test_cases = db.relationship("TestCase", secondary=test_cases, backref=db.backref('test_cases', lazy='dynamic'))

    test_suite_runs = db.relationship("TestSuiteRun", backref='test_suite', lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'short_name': self.short_name,
            'name': self.name,
            'description': self.description,
            'test_cases': self.serialize_test_cases(),
            'test_suite_runs': self.serialize_test_suite_runs()
        }

    def serialize_test_cases(self):
        return [item.serialize() for item in self.test_cases]

    def serialize_test_suite_runs(self):
        return [item.serialize() for item in self.test_suite_runs]

    def update_fields(self, json):
        self.short_name = json.get('short_name', None)
        self.name = json.get('name', None)
        self.description = json.get('description', None)
