from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.taught_skills.dto import (
    dto_new_existing_skills_response_item,
    dto_new_existing_skills_response
)



ns_taught_skills = Namespace("Existing and New Skills", validate=True)
ns_taught_skills.models[dto_new_existing_skills_response_item.name] = dto_new_existing_skills_response_item
ns_taught_skills.models[dto_new_existing_skills_response.name] = dto_new_existing_skills_response


@ns_taught_skills.route("/completions/<string:task_id>/taught_skills", endpoint="aims-taught-skills")
class GetTaughtSkills(Resource):     
    @ns_taught_skills.marshal_with(dto_new_existing_skills_response)
    @ns_taught_skills.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_taught_skills.response(int(HTTPStatus.NOT_FOUND), "Not Found error.")
    def get(self, task_id):   
            "Extract new skills and existing skills from the given learning unit."
            from search_l3s_aimeta.api.taught_skills.logic import TaughtSkills

            results = {
                    "task_id": task_id,
                    "new_skills": [ ],
                    "existing_skills": [ ] 
                    }
            try:
                mls_response = TaughtSkills.generate_skills(task_id)   
                return {"message": "success", "results": mls_response}, HTTPStatus.OK
                         
            except ValueError as e:
                return {"message": e.args[0], "results": results }, HTTPStatus.INTERNAL_SERVER_ERROR
            except FileExistsError as e:
                return {"message": e.args[0], "results": results}, HTTPStatus.NOT_FOUND
            except AssertionError as e:
                    return {"message": e.args[0], "results": results}, HTTPStatus.INTERNAL_SERVER_ERROR        





    