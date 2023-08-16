from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import request


sys.path.append('..')

from search_l3s_aimeta.api.trends.dto import (
    dataset_model,
    parameter_model,
    object_model,
    input_dataset_model
)



ns_trends = Namespace("Trends", validate=True)
ns_trends.models[dataset_model.name] = dataset_model
ns_trends.models[parameter_model.name] = parameter_model
ns_trends.models[object_model.name] = object_model
ns_trends.models[input_dataset_model.name] = input_dataset_model



@ns_trends.route("/trending-skills/", endpoint="trending-skills")
class GetTrends(Resource):     
    @ns_trends.doc(params={
        'loc': 'location',
        'job_name': 'name of the job',
        'radius': 'radius to search for jobs',
    })
    def get(self):   
            "Search for job offers"
            
            loc = request.args.get('loc')
            job_name = request.args.get('job_name')
            radius = request.args.get('radius')

            from search_l3s_aimeta.api.trends.logic import Trends
            jwt = Trends.get_jwt()

            results = Trends.search(jwt["access_token"], loc, job_name, radius)
            print("results", results)

            skills_compilation = Trends.formal_skills(jwt["access_token"], results["stellenangebote"])
            hist = Trends.create_formal_skill_histogram(skills_compilation)
            sorted_kv_list = sorted(hist.items(), key=lambda x:x[1], reverse=True)
            print("<skill>|<skill_level>|<context> --> <frequency>")
            for t in sorted_kv_list:
                print(t[0] +" --> "+ str(t[1]))

        
            return sorted_kv_list,  HTTPStatus.OK

    def post(self, id):
          mls_response = "testing"
          return mls_response, HTTPStatus.OK
    
    def delete(self, id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK
    
    def put(self, id):
        mls_response = "testing"
        return mls_response, HTTPStatus.OK





    