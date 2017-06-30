from sqlalchemy.orm import relationship

from taas.database import Model, db

test_parameters = db.Table(
    'test_parameter', Model.metadata,
    db.Column('test_case_id', db.Integer, db.ForeignKey('test_case.id')),
    db.Column('parameter_id', db.Integer, db.ForeignKey('parameter_group.id'))
)


class TestCase(Model):
    __tablename__ = 'test_case'

    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
    expected_success = db.Column(db.Boolean, default=True)
    test_runs = relationship("TestRun")
    parameters = relationship("TestParameter")
    steps = relationship("Step")
