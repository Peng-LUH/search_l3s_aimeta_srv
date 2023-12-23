from flask_restx import Model, fields

dto_content_tags_response_item = Model("DtoContentTagsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "content_tags": fields.List(fields.String, description='List of Content Tags', example=[
    "Arbeitsauftrag",
    "Ziele",
    "Funktion",
    "Bauteil",
    "Einzelteilzeichnung",
    "anspruchsvolles Werkstück",
    "Arbeitsfolge",
    "Form- und Lagetoleranzen",
    "Arbeitsplan"
  ])
})


dto_content_tags_response = Model('DtoContentTagsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_content_tags_response_item, description='Results')
                                        })
