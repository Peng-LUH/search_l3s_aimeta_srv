from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.dataset_preprocess.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)

from search_l3s_aimeta.api.dataset_preprocess.logic import Text_Preprocess


ns_dataset_preprocess = Namespace("Dataset Pre-process", validate=True)
ns_dataset_preprocess.models[dataset_model.name] = dataset_model
ns_dataset_preprocess.models[parameter_model.name] = parameter_model
ns_dataset_preprocess.models[object_model.name] = object_model
ns_dataset_preprocess.models[input_dataset_model.name] = input_dataset_model




@ns_dataset_preprocess.route("/preprocess-tasksteps/<string:id>", endpoint="preprocess_tasksteps")
class GetTaskSteps(Resource):
    #@ns_dataset_preprocess.expect(object_model)
    
    def get(self, id):    
        "Retrieve a Preprocessed TaskStep Resource"
    
        mls_response = Text_Preprocess.pre_process_taskstep(id)
        mls_response_json = mls_response
        
        return mls_response_json, HTTPStatus.OK



@ns_dataset_preprocess.route("/preprocess-tasks/<string:id>", endpoint="preprocess_tasks")
class GetTaskSteps(Resource):
    #@ns_dataset_preprocess.expect(object_model)
    
    def get(self, id):    
        "Retrieve a Preprocessed TaskStep Resource"
    
        mls_response = Text_Preprocess.pre_process_task(id)
        mls_response_json = mls_response
        
        return mls_response_json, HTTPStatus.OK

    