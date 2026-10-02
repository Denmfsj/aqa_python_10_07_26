from marshmallow import Schema, fields, validate


class StudentSchema(Schema):

    id = fields.Integer(required=True, strict=True, validate=validate.Range(min=1))
    name = fields.String(required=True, validate=validate.NoneOf(['Den', 'Alex']))
    score = fields.Integer(required=True, strict=True, validate=validate.Range(min=0, max=100))
    score_name = fields.String(required=True, allow_none=True) #, validate=validate.OneOf(['Bad', "ok", 'good']))
    created_date = fields.Float(required=True)
    updated_date = fields.DateTime(required=True)
