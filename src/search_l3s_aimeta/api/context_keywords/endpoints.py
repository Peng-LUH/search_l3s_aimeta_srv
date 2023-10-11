from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.context_keywords.dto import (
dto_context_tags_response
)



ns_context_keywords = Namespace("Context Keywords", validate=True)
ns_context_keywords.models[dto_context_tags_response.name] = dto_context_tags_response



@ns_context_keywords.route('/completions/<string:task_id>/context_tags', endpoint="aims_context_tags")
class GetContextKeywords(Resource): 
    
    def get(self, task_id):   
            "Retrieve Context Keywords of the Task"
            from search_l3s_aimeta.api.context_keywords.logic import ContextKeywords
 
    
            mls_response = ContextKeywords.generate_context_keywords(task_id)
        
            return mls_response, HTTPStatus.OK



    def post(self, task_id):
          mls_response = "testing"
          return mls_response, HTTPStatus.OK
    
    def delete(self, task_id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK
    
    def put(self, task_id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK

    