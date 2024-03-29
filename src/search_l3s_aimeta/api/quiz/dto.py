from flask_restx import Model, fields


quiz_item = Model('DtoQuizItem', {
    'Wissen': fields.List(fields.String, description='List of Wissen quiz questions',example =[
      "Welche Fragen sollen in der Reflexion besprochen werden?",
      "Welche Sicherheitsvorschriften sollten bei der Herstellung beachtet werden?"
    ]),
    'Verstehen': fields.List(fields.String, description='List of Verstehen quiz questions', example = [
      "Was sind die Ziele bei der Herstellung des Schlittens?",
      "Was ist die Funktion des Bauteils?"
    ]),
    'Anwenden': fields.List(fields.String, description='List of Anwenden quiz questions', example = [
      "Wie kannst du eine Arbeitsfolge planen, um die geforderten Toleranzen einzuhalten?",
      "Wie kannst du den Arbeitsplan ausformulieren, um den Schlitten in optimaler Qualität herzustellen?"
    ]),
})

dto_quiz_questions_response_item = Model("DtoQuizQuestionsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "quiz_questions": fields.Nested(quiz_item, description='Quiz questions categorized by taxonomy level')

})


dto_quiz_questions_response = Model('DtoQuizQuestionsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_quiz_questions_response_item, description='Results')
                                        })



