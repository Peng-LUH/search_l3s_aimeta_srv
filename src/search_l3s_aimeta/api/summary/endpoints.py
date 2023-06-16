from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

sys.path.append('..')

from search_l3s_aimeta.api.summary.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)



ns_summary = Namespace("Course Summary", validate=True)
ns_summary.models[dataset_model.name] = dataset_model
ns_summary.models[parameter_model.name] = parameter_model
ns_summary.models[object_model.name] = object_model
ns_summary.models[input_dataset_model.name] = input_dataset_model



@ns_summary.route("/task-summary/<string:id>", endpoint="summary")
class GetSummary(Resource): 
    
    def get(self, id):   
            "Retrieve a summary of the Task"
            from search_l3s_aimeta.api.summary.logic import Summary
    
            mls_response = Summary.generate_summary(id)
        
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



    