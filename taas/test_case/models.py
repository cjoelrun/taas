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

    def serialize(self):
        return {
            'id': self.id,
            'short_name': self.short_name,
            'name': self.name,
            'description': self.description,
            'expected_success': self.expected_success,
            'test_suite_id': self.test_suite_id,
            'test_runs': self.serialize_test_runs(),
            'steps': self.serialize_steps(),
            'parameters': self.serialize_parameters()
        }

    def serialize_test_runs(self):
        return [item.serialize() for item in self.test_runs]

    def serialize_steps(self):
        return [item.serialize() for item in self.steps]

    def serialize_parameters(self):
        return [item.serialize() for item in self.parameters]

    def update_fields(self, json):
        self.short_name = json.get('short_name', None)
        self.name = json.get('name', None)
        self.description = json.get('description', None)
        self.expected_success = json.get('expected_success', None)
        self.test_suite_id = json.get('test_suite_id', None)
