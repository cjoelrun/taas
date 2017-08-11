from taas.serialization import Schema
from taas.test_run.models import TestRun


class TestRunSchema(Schema):
    class Meta:
        model = TestRun


test_run_schema = TestRunSchema()
