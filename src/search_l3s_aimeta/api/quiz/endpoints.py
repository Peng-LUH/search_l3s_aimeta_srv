from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.quiz.dto import (
dto_quiz_questions_response
)



ns_quiz = Namespace("Quiz", validate=True)
ns_quiz.models[dto_quiz_questions_response.name] = dto_quiz_questions_response



@ns_quiz.route('/completions/<string:task_id>/quiz_questions', endpoint="aims_quiz_questions")
class GetQuiz(Resource): 

    def get(self, task_id):   
            "Generate a quiz of the Task"
            from search_l3s_aimeta.api.quiz.logic import Quiz
 
    
            mls_response = Quiz.generate_quiz(task_id)
        
            return mls_response, HTTPStatus.OK


    def post(self, task_id):
          mls_response = "testing"
          return mls_response, HTTPStatus.OK
    
    def delete(self, task_id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK
    
    def put(self, task_id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK


    