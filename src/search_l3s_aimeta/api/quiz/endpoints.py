from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.quiz.dto import (
dto_quiz_questions_response,
quiz_item
)



ns_quiz = Namespace("Quiz", validate=True)
ns_quiz.models[dto_quiz_questions_response.name] = dto_quiz_questions_response
ns_quiz.models[quiz_item.name] = quiz_item



@ns_quiz.route('/completions/<string:task_id>/quiz_questions', endpoint="aims_quiz_questions")
class GetQuiz(Resource): 
    @ns_quiz.marshal_with(dto_quiz_questions_response)
    def get(self, task_id):   
            "Generate a quiz of the Task"
            from search_l3s_aimeta.api.quiz.logic import Quiz
 
    
            mls_response = Quiz.generate_quiz(task_id)
        
            return {"task_id": task_id, "quiz": mls_response}, HTTPStatus.OK


 


    