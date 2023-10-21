from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.title.dto import (
dto_title_response
)



ns_title = Namespace("Course Title", validate=True)
ns_title.models[dto_title_response.name] = dto_title_response




@ns_title.route("/completions/<string:task_id>/title", endpoint="aims-title")
class GetTitle(Resource):     
    @ns_title.marshal_with(dto_title_response)
    def get(self, task_id):   
            "Generate Titles for the Task"
            from search_l3s_aimeta.api.title.logic import Title
 
            mls_response = Title.generate_title(task_id)
        
            return {"task_id": task_id, "title": mls_response}, HTTPStatus.OK





    