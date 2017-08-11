from taas.serialization import Schema
from taas.test_suite_run.models import TestSuiteRun


class TestSuiteRunSchema(Schema):
    class Meta:
        model = TestSuiteRun


test_suite_run_schema = TestSuiteRunSchema()
