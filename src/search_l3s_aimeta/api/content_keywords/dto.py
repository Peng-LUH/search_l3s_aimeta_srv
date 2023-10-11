from flask_restx import Model, fields



dto_content_tags_response = Model("DtoContentTagsResponse", {
    "unit_id": fields.String(),
    "content_tags": fields.List(fields.String())
})

