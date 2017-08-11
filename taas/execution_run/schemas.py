from taas.execution_run.models import ExecutionRun
from taas.serialization import Schema


class ExecutionRunSchema(Schema):
    class Meta:
        model = ExecutionRun

execution_run_schema = ExecutionRunSchema()
