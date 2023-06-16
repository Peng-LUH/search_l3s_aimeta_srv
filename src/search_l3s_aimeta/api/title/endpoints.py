from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.title.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)



ns_title = Namespace("Course Title", validate=True)
ns_title.models[dataset_model.name] = dataset_model
ns_title.models[parameter_model.name] = parameter_model
ns_title.models[object_model.name] = object_model
ns_title.models[input_dataset_model.name] = input_dataset_model



@ns_title.route("/course-title/<string:id>", endpoint="course-title")
class GetTitle(Resource):     
    def get(self, id):   
            "Generate Titles for the Task"
            from search_l3s_aimeta.api.title.logic import Title
 
            mls_response = Title.generate_title(id)
        
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





    