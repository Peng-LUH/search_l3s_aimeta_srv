from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort

sys.path.append('..')

from search_l3s_aimeta.api.dataset_preprocess.dto import (
    dto_task_preprocess_response,
    dto_taskstep_preprocess_response
)

from search_l3s_aimeta.api.dataset_preprocess.logic import Text_Preprocess


ns_dataset_preprocess = Namespace("Dataset Pre-process", validate=True)
ns_dataset_preprocess.models[dto_taskstep_preprocess_response.name] = dto_taskstep_preprocess_response
ns_dataset_preprocess.models[dto_task_preprocess_response.name] = dto_task_preprocess_response




@ns_dataset_preprocess.route("/preprocess-tasksteps/<string:taskstep_id>", endpoint="preprocess_tasksteps")
class GetTaskSteps(Resource):
    @ns_dataset_preprocess.marshal_with(dto_taskstep_preprocess_response)
    def get(self, taskstep_id):    
        "Retrieve a Preprocessed TaskStep Resource"
    

        try:
            assert int(taskstep_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
        except:
            abort(400, "Invalid type of task ID. Please try with valid task ID.")     
            
        mls_response = Text_Preprocess.pre_process_taskstep(taskstep_id)
        
        return mls_response, HTTPStatus.OK



@ns_dataset_preprocess.route("/preprocess-tasks/<string:task_id>", endpoint="preprocess_tasks")
class GetTask(Resource):
    @ns_dataset_preprocess.marshal_with(dto_task_preprocess_response)
    def get(self, task_id):    
        "Retrieve a Preprocessed TaskStep Resource"

        try:
            assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
        except:
            abort(400, "Invalid type of task ID. Please try with valid task ID.")        
    
        mls_response = Text_Preprocess.pre_process_task(task_id)
        
        return mls_response, HTTPStatus.OK

    