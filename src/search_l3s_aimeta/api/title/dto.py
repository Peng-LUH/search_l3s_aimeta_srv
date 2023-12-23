from flask_restx import Model, fields


dto_title_response_item = Model("DtoTitleResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "title": fields.List(fields.String, description='List of Titles for given task', example=[
    "Informiere dich über den Schlitten",
    "Plane den Bau des Schlittens",
    "Erstelle einen Arbeitsplan für den Schlittenbau"
  ])
})


dto_title_response = Model('DtoTitleResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_title_response_item, description='Results')
                                        })
