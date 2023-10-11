from flask_restx import Model, fields

dto_context_tags_response = Model("DtoContextTagsResponse", {
    "unit_id": fields.String(),
    "context_tags": fields.List(fields.String())
})

