from taas.serialization import Schema
from taas.step.models import Step


class StepSchema(Schema):
    class Meta:
        model = Step


step_schema = StepSchema()