from taas.execution.models import Execution
from taas.serialization import Schema


class ExecutionSchema(Schema):
    class Meta:
        model = Execution

execution_schema = ExecutionSchema()
