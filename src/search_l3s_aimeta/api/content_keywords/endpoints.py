from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.content_keywords.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)



ns_content_keywords = Namespace("Content Keywords", validate=True)
ns_content_keywords.models[dataset_model.name] = dataset_model
ns_content_keywords.models[parameter_model.name] = parameter_model
ns_content_keywords.models[object_model.name] = object_model
ns_content_keywords.models[input_dataset_model.name] = input_dataset_model



@ns_content_keywords.route("/content-keywords/<string:id>", endpoint="content-keywords")
class GetContentKeywords(Resource): 
    
    def get(self, id):  
            "Retrieve Content Keywords of the Task"
            from search_l3s_aimeta.api.content_keywords.logic import ContentKeywords
            
            mls_response = ContentKeywords.generate_content_keywords(id)
        
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



    