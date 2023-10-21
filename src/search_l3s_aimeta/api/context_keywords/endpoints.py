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
    @ns_context_keywords.marshal_with(dto_context_tags_response)
    def get(self, task_id):   
            "Retrieve Context Tags of the Task"
            from search_l3s_aimeta.api.context_keywords.logic import ContextKeywords
 
    
            mls_response = ContextKeywords.generate_context_keywords(task_id)
        
            return {"task_id":task_id, "context_tags": mls_response}, HTTPStatus.OK




    