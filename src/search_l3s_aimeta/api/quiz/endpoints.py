from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.quiz.dto import (
      quiz_item,
    dto_quiz_questions_response_item,
    dto_quiz_questions_response
        )

ns_quiz = Namespace("Quiz", validate=True)
ns_quiz.models[quiz_item.name] = quiz_item
ns_quiz.models[dto_quiz_questions_response_item.name] = dto_quiz_questions_response_item
ns_quiz.models[dto_quiz_questions_response.name] = dto_quiz_questions_response



@ns_quiz.route('/completions/<string:task_id>/quiz_questions', endpoint="aims_quiz_questions")
class GetQuiz(Resource): 
    @ns_quiz.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_quiz.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_quiz.marshal_with(dto_quiz_questions_response)
    def get(self, task_id):   
            "Generate a quiz of the Task"
            from search_l3s_aimeta.api.quiz.logic import Quiz

            results = {
                        "task_id": task_id,
                        "quiz_questions": {
                            "Wissen": [ ],
                            "Verstehen": [ ],
                            "Anwenden": [ ]
                                            }
                        }

            try:    
                mls_response = Quiz.generate_quiz(task_id)
                return {"message": "success", "results": mls_response}, HTTPStatus.OK
            
            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        



           


 


    