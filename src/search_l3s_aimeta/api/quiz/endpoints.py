from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


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

            try:
                assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
            except:
                     abort(400, "Invalid type of task ID. Please try with valid task ID.") 
    
            mls_response = Quiz.generate_quiz(task_id)
        
            return {"task_id": task_id, "quiz": mls_response}, HTTPStatus.OK


 


    