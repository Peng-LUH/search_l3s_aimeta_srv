from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort

sys.path.append('..')

from search_l3s_aimeta.api.context_keywords.dto import (
dto_context_tags_response_item,
dto_context_tags_response
)



ns_context_keywords = Namespace("Context Tags", validate=True)
ns_context_keywords.models[dto_context_tags_response.name] = dto_context_tags_response
ns_context_keywords.models[dto_context_tags_response_item.name] = dto_context_tags_response_item



parser_ns_context_keywords = ns_context_keywords.parser()
parser_ns_context_keywords.add_argument('task_id', type=str, help='Task ID', default=10, required=True)


@ns_context_keywords.route('/completions/<string:task_id>/context_tags', endpoint="aims_context_tags")
class GetContextKeywords(Resource): 
    @ns_context_keywords.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_context_keywords.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    @ns_context_keywords.marshal_with(dto_context_tags_response)
    def get(self, task_id):   
            "Retrieve Context Tags of the Task"
            from search_l3s_aimeta.api.context_keywords.logic import ContextKeywords
 
            results = {
                 "task_id": task_id,
                 "context_tags": []
                    }

            try:
                mls_response = ContextKeywords.generate_context_keywords(task_id)
                return {"message": "success", "results": mls_response}, HTTPStatus.OK

            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        




    