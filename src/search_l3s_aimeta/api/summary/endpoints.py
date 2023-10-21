from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys

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
    
            mls_response = Summary.generate_summary(task_id)
        
            return {"task_id":task_id,"summary": mls_response}, HTTPStatus.OK




    