from flask_restx import Model, fields

dto_quiz_questions_response = Model("DtoQuizQuestionsResponse", {
    "unit_id": fields.String(),
    "quiz_questions": fields.List(fields.String())
})