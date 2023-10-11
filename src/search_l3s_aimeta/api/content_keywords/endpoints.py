from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.content_keywords.dto import (
    dto_content_tags_response
)



ns_content_keywords = Namespace("Content Keywords", validate=True)
ns_content_keywords.models[dto_content_tags_response.name] = ns_content_keywords



@ns_content_keywords.route('/completions/<string:task_id>/content_tags', endpoint="aims_content_tags")
class GetContentKeywords(Resource): 
    
    def get(self, task_id):  
            "Retrieve Content Keywords of the Task"
            from search_l3s_aimeta.api.content_keywords.logic import ContentKeywords
            
            mls_response = ContentKeywords.generate_content_keywords(task_id)
        
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



    