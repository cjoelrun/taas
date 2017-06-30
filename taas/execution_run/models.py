from taas.database import Model, db


class ExecutionRun(Model):
    __tablename__ = 'execution_run'

    test_run_id = db.Column(db.Integer, db.ForeignKey('test_case.id'), primary_key=True)
    step_id = db.Column(db.Integer, db.ForeignKey('execution.id'), primary_key=True)
    message = db.Column(db.String)
    context = db.Column(db.String)
    status = db.Column(db.String)
