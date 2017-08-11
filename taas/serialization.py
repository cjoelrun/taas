from flask_marshmallow import Marshmallow

ma = Marshmallow()


class Schema(ma.ModelSchema):
    __abstract__ = True
