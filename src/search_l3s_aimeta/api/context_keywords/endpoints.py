from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort

sys.path.append('..')

from search_l3s_aimeta.api.context_keywords.dto import (
dto_context_tags_response
)



ns_context_keywords = Namespace("Context Keywords", validate=True)
ns_context_keywords.models[dto_context_tags_response.name] = dto_context_tags_response



parser_ns_context_keywords = ns_context_keywords.parser()
parser_ns_context_keywords.add_argument('task_id', type=str, help='Task ID', default=10, required=True)


@ns_context_keywords.route('/completions/<string:task_id>/context_tags', endpoint="aims_context_tags")
class GetContextKeywords(Resource): 
    @ns_context_keywords.marshal_with(dto_context_tags_response)
    def get(self, task_id):   
            "Retrieve Context Tags of the Task"
            from search_l3s_aimeta.api.context_keywords.logic import ContextKeywords
 
            try:
                assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
            except:
                     abort(400, "Invalid type of task ID. Please try with valid task ID.")
    
            mls_response = ContextKeywords.generate_context_keywords(task_id)
        
            return {"task_id":task_id, "context_tags": mls_response}, HTTPStatus.OK




    