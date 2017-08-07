from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from taas.database import Model, db


class TestRun(Model):
    id = db.Column(db.Integer, primary_key=True)
    test_case_id = db.Column(db.ForeignKey("test_case.id"))
    message = db.Column(db.String)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    # TODO: Constrain
    status = db.Column(db.String)
    runtime_data = db.Column(JSONB)

    execution_runs = relationship("ExecutionRun", backref='TestRun')

    def serialize(self):
        return {
            'id': self.id,
            'test_case_id': self.test_case_id,
            'message': self.message,
            'start_time': '',  # TODO
            'end_time': '',  # TODO
            'status': self.status,
            'runtime_data': self.runtime_data,
            'execution_runs': self.serialize_execution_runs()
        }

    def serialize_execution_runs(self):
        """
       Return object's relations in easily serializeable format.
       NB! Calls many2many's serialize property.
       """
        # return [item.serialize() for item in self.many2many]
        return []
