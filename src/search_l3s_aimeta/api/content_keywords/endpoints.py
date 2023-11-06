from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort

sys.path.append('..')

from search_l3s_aimeta.api.content_keywords.dto import (
    dto_content_tags_response
)



ns_content_keywords = Namespace("Content Keywords", validate=True)
ns_content_keywords.models[dto_content_tags_response.name] = dto_content_tags_response



@ns_content_keywords.route('/completions/<string:task_id>/content_tags', endpoint="aims_content_tags")
class GetContentKeywords(Resource): 
    @ns_content_keywords.marshal_with(dto_content_tags_response)
    def get(self, task_id):  
            "Retrieve Content tags of the Task"
            from search_l3s_aimeta.api.content_keywords.logic import ContentKeywords
            

            mls_response = ContentKeywords.generate_content_keywords(task_id)

            return {"task_id":task_id, "content_tags": mls_response}, HTTPStatus.OK    
                    

 



    