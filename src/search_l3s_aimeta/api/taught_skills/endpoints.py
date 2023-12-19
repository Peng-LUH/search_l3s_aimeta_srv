from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.taught_skills.dto import (
    dto_new_existing_skills_response
)



ns_taught_skills = Namespace("Existing and New Skills", validate=True)
ns_taught_skills.models[dto_new_existing_skills_response.name] = dto_new_existing_skills_response


@ns_taught_skills.route("/completions/<string:task_id>/taught_skills", endpoint="aims-taught-skills")
class GetTitle(Resource):     
    @ns_taught_skills.marshal_with(dto_new_existing_skills_response)
    def get(self, task_id):   
            "Extract new skills and existing skills from the given learning unit."
            from search_l3s_aimeta.api.taught_skills.logic import TaughtSkills

            try:
                assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
            except:
                     abort(400, "Invalid type of task ID. Please try with valid task ID.")   
            mls_response = TaughtSkills.generate_skills(task_id)                            

            try: 
                return mls_response, HTTPStatus.OK
            except:
                  abort(400, "Invalid response. Please try again.")



    