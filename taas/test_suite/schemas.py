from taas.serialization import Schema
from taas.test_suite.models import TestSuite


class TestSuiteSchema(Schema):
    class Meta:
        model = TestSuite


test_suite_schema = TestSuiteSchema()
