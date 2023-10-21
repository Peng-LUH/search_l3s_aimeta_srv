from flask_restx import Model, fields


dto_title_response = Model("DtoTitleResponse", {
    "task_id": fields.String(description='The task ID', example='10'),
    "title": fields.List(fields.String, description='List of Titles for given task', example=[
    "Informiere dich über den Schlitten!",
    "Plane den Bau des Schlittens!",
    "Erstelle einen Arbeitsplan für den Schlittenbau!"
  ])
})

