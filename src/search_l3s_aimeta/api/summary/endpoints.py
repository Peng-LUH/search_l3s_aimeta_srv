from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.summary.dto import (
dto_summary_response
)



ns_summary = Namespace("Course Summary", validate=True)
ns_summary.models[dto_summary_response.name] = dto_summary_response




@ns_summary.route("/completions/<string:task_id>/summary", endpoint="aims_summary")
class GetSummary(Resource): 
    @ns_summary.marshal_with(dto_summary_response)
    def get(self, task_id):   
            "Retrieve a summary of the Task"
            from search_l3s_aimeta.api.summary.logic import Summary

            try:
                assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
            except:
                     abort(400, "Invalid type of task ID. Please try with valid task ID.")    
            mls_response = Summary.generate_summary(task_id)
        
            return {"task_id":task_id,"summary": mls_response}, HTTPStatus.OK




    