from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.learning_goal.dto import (
    dto_learning_goal_response
)



ns_learning_goal = Namespace("Learning Goal", validate=True)
ns_learning_goal.models[dto_learning_goal_response.name] = dto_learning_goal_response




@ns_learning_goal.route('/completions/<string:task_id>/learning_goal', endpoint="aims_learning_goal")
class GetLearningGoal(Resource): 
    @ns_learning_goal.marshal_with(dto_learning_goal_response)
    def get(self, task_id):   
            "Retrieve Learnng Goals of the Task"
            from search_l3s_aimeta.api.learning_goal.logic import LearningGoal
 
            mls_response = LearningGoal.generate_learning_goal(task_id)
        
            return {"task_id":task_id, "learning_goal":mls_response}, HTTPStatus.OK




    