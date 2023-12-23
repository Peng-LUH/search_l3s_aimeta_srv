from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.title.dto import (
dto_title_response_item,
dto_title_response
)



ns_title = Namespace("Course Title", validate=True)
ns_title.models[dto_title_response_item.name] = dto_title_response_item
ns_title.models[dto_title_response.name] = dto_title_response




@ns_title.route("/completions/<string:task_id>/title", endpoint="aims-title")
class GetTitle(Resource):    
    @ns_title.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_title.response(int(HTTPStatus.NOT_FOUND), "Not Found error.") 
    @ns_title.marshal_with(dto_title_response)
    def get(self, task_id):   
            "Generate Titles for the Task"
            from search_l3s_aimeta.api.title.logic import Title

            results = {
                 "task_id": task_id,
                 "title": []
                    }

            try:
                mls_response = Title.generate_title(task_id)
                return {"message": "success", "results": mls_response}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        






    