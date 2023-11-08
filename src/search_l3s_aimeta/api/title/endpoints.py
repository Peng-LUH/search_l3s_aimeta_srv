from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


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

            try:
                assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
            except:
                     abort(400, "Invalid type of task ID. Please try with valid task ID.")   
            mls_response = Title.generate_title(task_id)
        
            return {"task_id": task_id, "title": mls_response}, HTTPStatus.OK





    