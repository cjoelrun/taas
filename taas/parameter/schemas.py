from taas.parameter.models import Parameter
from taas.serialization import Schema


class ParameterSchema(Schema):
    class Meta:
        model = Parameter

parameter_schema = ParameterSchema()
