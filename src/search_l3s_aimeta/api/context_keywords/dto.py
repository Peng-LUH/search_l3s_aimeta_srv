from flask_restx import Model, fields

dto_context_tags_response_item = Model("DtoContextTagsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "context_tags": fields.List(fields.String, description='List of Context Tags', example=["Arbeitsplanung", "Herstellung", "Reflexion", "Erfolgskontrolle"
                                                                                            ])
})




dto_context_tags_response = Model('DtoContextTagsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_context_tags_response_item, description='Results')
                                        })
