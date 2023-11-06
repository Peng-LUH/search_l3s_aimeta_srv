from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import request
from flask_cors import cross_origin


sys.path.append('..')

from search_l3s_aimeta.api.trends.dto import (
    dto_skills_request,
    dto_jobs_search_request,
    dto_trending_skills_request,
    dto_jobs_search_response,
    dto_skills_response,
    dto_trending_skills_response,
)



ns_trends = Namespace("Trends", validate=True)
ns_trends.models[dto_skills_request.name] = dto_skills_request
ns_trends.models[dto_jobs_search_request.name] = dto_jobs_search_request
ns_trends.models[dto_trending_skills_request.name] = dto_trending_skills_request
ns_trends.models[dto_jobs_search_response.name] = dto_jobs_search_response
ns_trends.models[dto_skills_response.name] = dto_skills_response
ns_trends.models[dto_trending_skills_response.name] = dto_trending_skills_response


@ns_trends.route("/search-jobs/", endpoint="search-jobs")
class SearchJobs(Resource):   
    @ns_trends.marshal_list_with(dto_jobs_search_response)
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
            trend = Trends()

            jwt = trend.get_jwt()

            results = trend.search(jwt["access_token"], job_name, loc,  radius)

            # skills_compilation = trend.formal_skills(jwt["access_token"], results["stellenangebote"])
            # hist = trend.create_formal_skill_histogram(skills_compilation)
            # sorted_kv_list = sorted(hist.items(), key=lambda x:x[1], reverse=True)
            # print("<skill>|<skill_level>|<context> --> <frequency>")
            # for t in sorted_kv_list:
            #     print(t[0] +" --> "+ str(t[1]))

        
            return {"job_offers": results['stellenangebote'] },  HTTPStatus.OK




@ns_trends.route("/skills/", endpoint="skills")
class GetSkills(Resource):   
    #@ns_trends.marshal_with(dto_skills_response)
    @ns_trends.doc(params={
        'loc': 'location',
        'job_name': 'name of the job',
        'radius': 'radius to search for jobs',
    })
    def get(self):   
            "get skills"            
            loc = request.args.get('loc')
            job_name = request.args.get('job_name')
            radius = request.args.get('radius')

            from search_l3s_aimeta.api.trends.logic import Trends
            trend = Trends()

            jwt = trend.get_jwt()

            results = trend.search(jwt["access_token"], job_name, loc, radius)

            skills_compilation = trend.formal_skills(jwt["access_token"], results["stellenangebote"])

        
            return {"skill": skills_compilation},  HTTPStatus.OK
    





@ns_trends.route("/trending-skills/", endpoint="trending-skills")
class GetTrends(Resource):   
    #@ns_trends.marshal_with(dto_trending_skills_response)  
    @ns_trends.doc(params={
        'loc': 'location',
        'job_name': 'name of the job',
        'radius': 'radius to search for jobs',
    })
    def get(self):   
            "trending skills"            
            loc = request.args.get('loc')
            job_name = request.args.get('job_name')
            radius = request.args.get('radius')

            from search_l3s_aimeta.api.trends.logic import Trends
            trend = Trends()

            jwt = trend.get_jwt()

            results = trend.search(jwt["access_token"], job_name, loc, radius)

            skills_compilation = trend.formal_skills(jwt["access_token"], results["stellenangebote"])
            hist = trend.create_formal_skill_histogram(skills_compilation)

            sorted_kv_list = sorted(hist.items(), key=lambda x:x[1], reverse=True)

            #print(sorted_kv_list)

            # for t in sorted_kv_list:
            #     print(t[0] +" --> "+ str(t[1]))


        
            return {"trending_skills": sorted_kv_list},  HTTPStatus.OK
