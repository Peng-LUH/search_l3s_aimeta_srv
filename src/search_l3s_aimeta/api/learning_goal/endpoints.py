from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.learning_goal.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)



ns_learning_goal = Namespace("Learning Goal", validate=True)
ns_learning_goal.models[dataset_model.name] = dataset_model
ns_learning_goal.models[parameter_model.name] = parameter_model
ns_learning_goal.models[object_model.name] = object_model
ns_learning_goal.models[input_dataset_model.name] = input_dataset_model



@ns_learning_goal.route("/learning-goal/<string:id>", endpoint="learning-goal")
class GetLearningGoal(Resource): 
    
    def get(self, id):   
            "Retrieve Learnng Goals of the Task"
            from search_l3s_aimeta.api.learning_goal.logic import LearningGoal
 
            mls_response = LearningGoal.generate_learning_goal(id)
        
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



    