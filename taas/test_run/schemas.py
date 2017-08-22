from taas.serialization import Schema
from taas.test_run.models import TestRun


class TestRunSchema(Schema):
    class Meta:
        model = TestRun
        include_fk = True


test_run_schema = TestRunSchema()
