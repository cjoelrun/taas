from taas.parameter_group.models import ParameterGroup
from taas.serialization import Schema


class ParameterGroupSchema(Schema):
    class Meta:
        model = ParameterGroup

parameter_group_schema = ParameterGroupSchema()
