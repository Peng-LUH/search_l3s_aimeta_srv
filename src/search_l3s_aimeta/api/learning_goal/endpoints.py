from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.learning_goal.dto import (
    dto_learning_goal_response_item,
    dto_learning_goal_response
)



ns_learning_goal = Namespace("Learning Goal", validate=True)
ns_learning_goal.models[dto_learning_goal_response.name] = dto_learning_goal_response
ns_learning_goal.models[dto_learning_goal_response_item.name] = dto_learning_goal_response_item



@ns_learning_goal.route('/completions/<string:task_id>/learning_goal', endpoint="aims_learning_goal")
class GetLearningGoal(Resource): 
    @ns_learning_goal.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_learning_goal.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_learning_goal.marshal_with(dto_learning_goal_response)
    def get(self, task_id):   
            "Retrieve Learnng Goals of the Task"
            from search_l3s_aimeta.api.learning_goal.logic import LearningGoal
 
            results = {
                 "task_id": task_id,
                 "learning_goals": []
                    }

            try: 
                mls_response = LearningGoal.generate_learning_goal(task_id)
                return {"message": "success", "results": mls_response}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        





    