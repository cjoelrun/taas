from taas.database import Model, db


class ExecutionRun(Model):
    test_run_id = db.Column(db.Integer, db.ForeignKey('test_run.id'), primary_key=True)
    step_id = db.Column(db.Integer, db.ForeignKey('step.id'), primary_key=True)
    message = db.Column(db.String)
    context = db.Column(db.String)
    status = db.Column(db.String)
