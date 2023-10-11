from flask_restx import Model, fields


dto_title_response = Model("DtoTitleResponse", {
    "unit_id": fields.String(),
    "title": fields.List(fields.String())
})

