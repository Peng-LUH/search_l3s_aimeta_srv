from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort

sys.path.append('..')

from search_l3s_aimeta.api.dataset_preprocess.dto import (
    dto_task_preprocess_response,
    dto_task_preprocess_response_item,
    dto_taskstep_preprocess_response,
    dto_taskstep_preprocess_response_item
)

from search_l3s_aimeta.api.dataset_preprocess.logic import Text_Preprocess


ns_dataset_preprocess = Namespace("Dataset Pre-process", validate=True)
ns_dataset_preprocess.models[dto_taskstep_preprocess_response_item.name] = dto_taskstep_preprocess_response_item
ns_dataset_preprocess.models[dto_taskstep_preprocess_response.name] = dto_taskstep_preprocess_response
ns_dataset_preprocess.models[dto_task_preprocess_response_item.name] = dto_task_preprocess_response_item
ns_dataset_preprocess.models[dto_task_preprocess_response.name] = dto_task_preprocess_response




@ns_dataset_preprocess.route("/preprocess-tasksteps/<string:taskstep_id>", endpoint="preprocess_tasksteps")
class GetTaskSteps(Resource):
    @ns_dataset_preprocess.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_dataset_preprocess.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_dataset_preprocess.marshal_with(dto_taskstep_preprocess_response)
    def get(self, taskstep_id):    
        "Retrieve a Preprocessed TaskStep Resource"

        results = {
                "taskstep_id": taskstep_id,
                "taskstep_text": " "
            }
    
        try:    
            mls_response = Text_Preprocess.pre_process_taskstep(taskstep_id)
            return {"message": "success", "results": mls_response}, HTTPStatus.OK

        except ValueError as e:
            return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        



@ns_dataset_preprocess.route("/preprocess-tasks/<string:task_id>", endpoint="preprocess_tasks")
class GetTask(Resource):
    @ns_dataset_preprocess.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_dataset_preprocess.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_dataset_preprocess.marshal_with(dto_task_preprocess_response)
    def get(self, task_id):    
        "Retrieve a Preprocessed TaskStep Resource"
        results  = {
            "task_id": task_id,
            "task_title": ' ',
            "text": ' ',
            "tasksteps_ids": [],
            "task_set_id": ' '
            }
        
        try: 
            mls_response = Text_Preprocess.pre_process_task(task_id)
            return {"message": "success", "results": mls_response}, HTTPStatus.OK
        except ValueError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileExistsError as e:
            return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
        except AssertionError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        

    