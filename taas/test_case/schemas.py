from taas.serialization import Schema
from taas.test_case.models import TestCase


class TestCaseSchema(Schema):
    class Meta:
        model = TestCase


test_case_schema = TestCaseSchema()
