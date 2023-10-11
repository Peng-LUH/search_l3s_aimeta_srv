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
    def get(self, task_id):   
            "Generate Titles for the Task"
            from search_l3s_aimeta.api.title.logic import Title
 
            mls_response = Title.generate_title(task_id)
        
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





    