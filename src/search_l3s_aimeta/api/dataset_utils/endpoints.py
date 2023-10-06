from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

from search_l3s_aimeta.api.dataset_utils.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)

from search_l3s_aimeta.api.dataset_utils.logic.mls_processor import MLSConnector, MLSCorpus

from search_l3s_aimeta.api.dataset_utils.logic.preprocessor import dataset_json2jsonl

ns_dataset_generator = Namespace("MLS Tasks", validate=True)
ns_dataset_generator.models[dataset_model.name] = dataset_model
ns_dataset_generator.models[parameter_model.name] = parameter_model
ns_dataset_generator.models[object_model.name] = object_model
ns_dataset_generator.models[input_dataset_model.name] = input_dataset_model

# @ns_dataset_generator.route("/mls-content-type", endpoint="mls_content_type")
# class MlsContentType(Resource):
#     def get(self):
#         "Retrieve valid mls content type for generating corpus"
#         content_type = MLSConnector.VALID_CONTENT_TYPE
#         content_type_json = json.dumps(content_type)
        
#         return content_type, HTTPStatus.OK


@ns_dataset_generator.route("/mls-response-dataset", endpoint="mls_response_dataset")
class MlsResponse(Resource):
    @ns_dataset_generator.expect(dataset_model)
    def post(self):
        request_data = ns_dataset_generator.payload
        dataset_name = request_data.get("name")
        dataset_parameters = request_data.get("parameters")
        
        mls_response = MLSConnector.get_dataset_response(dataset_name, parameters=dataset_parameters)
        mls_response_json = mls_response.json()
        return mls_response_json, HTTPStatus.CREATED


@ns_dataset_generator.route("/mls-response-object", endpoint="mls_response_object")
class MlsResponse(Resource):
    @ns_dataset_generator.expect(object_model)
    def post(self):
        object_id = ns_dataset_generator.payload.get("object_id")
        
        mls_response = MLSConnector.get_object_response(object_id)
        mls_response_json = mls_response.json()
        
        return mls_response_json, HTTPStatus.CREATED
    

# @ns_dataset_generator.route("/mls-corpus", endpoint="dataset_generator_mls")
# class GenerateMlsDataset(Resource):
#     @ns_dataset_generator.expect(dataset_model)
#     @ns_dataset_generator.response(int(HTTPStatus.CREATED), description="Successfully created json file")
#     @ns_dataset_generator.response(int(HTTPStatus.BAD_REQUEST), description="Request error, e.g., wrong corpus name")
#     # @ns_dataset_generator.marshal_list_with(document_model)
#     def post(self):
#         """retrieval mls dataset and save as json file"""
#         request_data = ns_dataset_generator.payload
#         dataset_name = request_data.get("name")
#         dataset_parameters = request_data.get("parameters")
        
#         mls_response = MLSConnector.get_dataset_response(dataset_name, parameters=dataset_parameters)
#         mls_response_json = mls_response.json()
        
#         corpus_json = MLSCorpus.corpus_generator(mls_response_json)
        
        
#         # res = {
#         #     "message": "Success",
#         #     "corpus_name": dataset_name,
#         #     "context": mls_response_json.get("@context"),
#         #     "dataset": mls_response_json.get("hydra:member")
#         # }
#         return corpus_json, HTTPStatus.CREATED


# @ns_dataset_generator.route("/json-to-jsonl-converter", endpoint="json_to_jsonl_converter")
# class JsonToJsonl(Resource):
#     @ns_dataset_generator.expect(input_dataset_model)
#     def post(self):
#         dataset_name = ns_dataset_generator.payload.get("dataset_name")

#         if not dataset_name:
#             raise ValueError("Dataset name is empty!")
        
#         result = dataset_json2jsonl(dataset_name)
        
#         if result == 1:
#             return {"message": "Success"}, HTTPStatus.CREATED
#         else:
#             return result.get("error"), result.get("code")
    

# @ns_dataset_generator.route("/get-datasets-name", endpoint="get_dataset_name")
# class GetDatasetName(Resource):
#     def get(self):
#         return {"message": "Success"}, HTTPStatus.OK
    

@ns_dataset_generator.route("/get-tasksteps/<string:id>", endpoint="get_tasksteps")
class GetTaskSteps(Resource):
    #@ns_dataset_generator.expect(object_model)
    
    def get(self, id):    
        "Retrieve a TaskStep Resource"
    
        mls_response = MLSConnector.get_task_steps_response(id)
        mls_response_json = mls_response.json()
        
        return mls_response_json, HTTPStatus.OK
    

@ns_dataset_generator.route("/get-tasks/<string:id>", endpoint="get_tasks")
class GetTaskSteps(Resource):
    #@ns_dataset_generator.expect(object_model)
    def get(self, id):     
        "Retrieve a Task resource"
       
        mls_response = MLSConnector.get_task_response(id)
        mls_response_json = mls_response.json()
        
        return mls_response_json, HTTPStatus.OK
