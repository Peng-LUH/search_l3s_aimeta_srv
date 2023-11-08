from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort

from search_l3s_aimeta.api.dataset_utils.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)

from search_l3s_aimeta.api.dataset_utils.logic.mls_processor import MLSConnector


ns_dataset_generator = Namespace("MLS Tasks", validate=True)
ns_dataset_generator.models[dataset_model.name] = dataset_model
ns_dataset_generator.models[parameter_model.name] = parameter_model
ns_dataset_generator.models[object_model.name] = object_model
ns_dataset_generator.models[input_dataset_model.name] = input_dataset_model

    

@ns_dataset_generator.route("/get-tasks/<string:task_id>", endpoint="get_tasks")
class GetTaskSteps(Resource):
    #@ns_dataset_generator.expect(object_model)
    def get(self, task_id):     
        "Retrieve a Task resource"

        try:
            assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
        except:
            abort(400, "Invalid type of task ID. Please try with valid task ID.")     
            
       
        mls_response = MLSConnector.get_task_response(task_id)
        mls_response_json = mls_response.json()
        
        return mls_response_json, HTTPStatus.OK
    


@ns_dataset_generator.route("/get-tasksteps/<string:taskstep_id>", endpoint="get_tasksteps")
class GetTaskSteps(Resource):
    #@ns_dataset_generator.expect(object_model)
    
    def get(self, taskstep_id):    
        "Retrieve a TaskStep Resource"


        try:
            assert int(taskstep_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
        except:
            abort(400, "Invalid type of task ID. Please try with valid task ID.")     
            
    
        mls_response = MLSConnector.get_task_steps_response(taskstep_id)
        mls_response_json = mls_response.json()
        
        return mls_response_json, HTTPStatus.OK