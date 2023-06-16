from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.quiz.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)



ns_quiz = Namespace("Quiz", validate=True)
ns_quiz.models[dataset_model.name] = dataset_model
ns_quiz.models[parameter_model.name] = parameter_model
ns_quiz.models[object_model.name] = object_model
ns_quiz.models[input_dataset_model.name] = input_dataset_model



@ns_quiz.route("/quiz/<string:id>", endpoint="quiz")
class GetQuiz(Resource): 

    def get(self, id):   
            "Generate a quiz of the Task"
            from search_l3s_aimeta.api.quiz.logic import Quiz
 
    
            mls_response = Quiz.generate_quiz(id)
        
            return mls_response, HTTPStatus.OK


    def post(self, id):
          mls_response = "testing"
          return mls_response, HTTPStatus.OK
    
    def delete(self, id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK
    
    def put(self, id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK


    