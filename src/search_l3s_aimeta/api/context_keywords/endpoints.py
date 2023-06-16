from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.summary.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)



ns_context_keywords = Namespace("Context Keywords", validate=True)
ns_context_keywords.models[dataset_model.name] = dataset_model
ns_context_keywords.models[parameter_model.name] = parameter_model
ns_context_keywords.models[object_model.name] = object_model
ns_context_keywords.models[input_dataset_model.name] = input_dataset_model



@ns_context_keywords.route("/context-keywords/<string:id>", endpoint="context-keywords")
class GetContextKeywords(Resource): 
    
    def get(self, id):   
            "Retrieve Context Keywords of the Task"
            from search_l3s_aimeta.api.context_keywords.logic import ContextKeywords
 
    
            mls_response = ContextKeywords.generate_context_keywords(id)
        
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

    