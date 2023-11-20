from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import abort


sys.path.append('..')

from search_l3s_aimeta.api.taught_skills.dto import (
    dto_taught_skills_response,
    dto_existing_skills_response
)



ns_taught_skills = Namespace("Taught and New Skill", validate=True)
ns_taught_skills.models[dto_taught_skills_response.name] = dto_taught_skills_response
ns_taught_skills.models[dto_existing_skills_response.name] = dto_existing_skills_response


@ns_taught_skills.route("/completions/<string:task_id>/taught_skills", endpoint="aims-taught-skills")
class GetTitle(Resource):     
    @ns_taught_skills.marshal_with(dto_taught_skills_response)
    def get(self, task_id):   
            "Generate new taught skills and retrieve existing skills"
            from search_l3s_aimeta.api.taught_skills.logic import TaughtSkills

            try:
                assert int(task_id)>0, abort(400, "Invalid type of task ID. Please try with positive integer.")
            except:
                     abort(400, "Invalid type of task ID. Please try with valid task ID.")   
            mls_response = TaughtSkills.generate_skills(task_id)
        
            return {"task_id": task_id, "new_skills": mls_response}, HTTPStatus.OK



    