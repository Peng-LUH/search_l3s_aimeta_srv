from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.summary.dto import (
    dto_summary_response_item,
    dto_summary_response
    )



ns_summary = Namespace("Course Summary", validate=True)
ns_summary.models[dto_summary_response.name] = dto_summary_response
ns_summary.models[dto_summary_response_item.name] = dto_summary_response_item




@ns_summary.route("/completions/<string:task_id>/summary", endpoint="aims_summary")
class GetSummary(Resource): 
    @ns_summary.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_summary.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_summary.marshal_with(dto_summary_response)
    def get(self, task_id):   
            "Retrieve a summary of the Task"
            from search_l3s_aimeta.api.summary.logic import Summary

            results = {
                 "task_id": task_id,
                 "summary": ''
                    }
            try: 
                mls_response = Summary.generate_summary(task_id)   
                return {"message": "success", "results": mls_response}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        




    