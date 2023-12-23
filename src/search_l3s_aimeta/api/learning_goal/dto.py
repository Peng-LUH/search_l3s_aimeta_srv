from flask_restx import Model, fields

dto_learning_goal_response_item = Model("DtoLearningGoalResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "learning_goals": fields.List(fields.String, description='List of learning goals', example=[
        "Die Funktion des Bauteils 'Schlitten' verstehen",
        "Einen effektiven Arbeitsplan für die Herstellung des Schlittens erstellen",
        "Den Schlitten sicher und effektiv herstellen und dabei Form- und Lagetoleranzen einhalten"
    ])
})


dto_learning_goal_response = Model('DtoLearningGoalResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_learning_goal_response_item, description='Results')
                                        })