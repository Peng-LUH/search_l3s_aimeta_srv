from flask_restx import Model, fields

dto_context_tags_response = Model("DtoContextTagsResponse", {
    "task_id": fields.String(description='The task ID', example='10'),
    "context_tags": fields.List(fields.String, description='List of Context Tags', example=["Arbeitsplanung", "Herstellung", "Reflexion", "Erfolgskontrolle"
                                                                                            ])
})