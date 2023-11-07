from http import HTTPStatus
import json
from flask_restx import Namespace, Resource
import sys
from flask import request, abort
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

            try:
                jwt = trend.get_jwt()
            except:
                  abort(501, "Connection to arbeitsagentur is not available.")    

            assert "access_token" in jwt.keys(), abort(501, "Invalid Access token. Connection to arbeitsagentur is not available.")        

            results = trend.search(jwt["access_token"], job_name, loc,  radius)

            assert "stellenangebote" in results.keys(), abort(400,f"No job offers for job name: '{job_name}' at location: '{loc}'")

            return {"job_offers": results['stellenangebote'] },  HTTPStatus.OK




@ns_trends.route("/skills/", endpoint="skills")
class GetSkills(Resource):   
    @ns_trends.marshal_with(dto_skills_response)
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

            try:
                jwt = trend.get_jwt()
            except:
                  abort(501, "Connection to arbeitsagentur is not available.")    

            assert "access_token" in jwt.keys(), abort(501, "Invalid Access token. Connection to arbeitsagentur is not available.")        

            results = trend.search(jwt["access_token"], job_name, loc, radius)

            assert "stellenangebote" in results.keys(), abort(400,f"No job offers for job name: '{job_name}' at location: '{loc}'")

            skills_compilation = trend.formal_skills(jwt["access_token"], results["stellenangebote"])

            assert len(skills_compilation)>0, abort(400,f"No Skills for job name: '{job_name}' at location: '{loc}'")

        
            return {"skills": skills_compilation},  HTTPStatus.OK
    





@ns_trends.route("/trending-skills/", endpoint="trending-skills")
class GetTrends(Resource):   
    @ns_trends.marshal_with(dto_trending_skills_response)  
    @ns_trends.doc(params={
        'loc': 'location',
        'job_name': 'name of the job',
        'radius': 'radius to search for jobs',
        'topk': 'top k trending skills'
    })
    def get(self):   
            "get trending skills"            
            loc = request.args.get('loc')
            job_name = request.args.get('job_name')
            radius = request.args.get('radius')
            topk = int(request.args.get('topk'))


            from search_l3s_aimeta.api.trends.logic import Trends
            trend = Trends()

            try:
                jwt = trend.get_jwt()
            except:
                  abort(501, "Connection to arbeitsagentur is not available.")    

            assert "access_token" in jwt.keys(), abort(501, "Invalid Access token. Connection to arbeitsagentur is not available.")        

            results = trend.search(jwt["access_token"], job_name, loc, radius)

            assert "stellenangebote" in results.keys(), abort(400,f"No job offers for job name: '{job_name}' at location: '{loc}'")

            skills_compilation = trend.formal_skills(jwt["access_token"], results["stellenangebote"])

            assert len(skills_compilation)>0, abort(400,f"No Trending Skills for job name: '{job_name}' at location: '{loc}'")


            hist = trend.create_formal_skill_histogram(skills_compilation)

            assert len(hist)>0, abort(400,f"No Trending Skills for job name: '{job_name}' at location: '{loc}'")


            sorted_kv_list = sorted(hist.items(), key=lambda x:x[1], reverse=True)

            if len(sorted_kv_list)>topk:
                  sorted_kv_list = sorted_kv_list[:topk]
            else:
                  topk = len(sorted_kv_list)  

            top_k_trending_skills = []

            for skill in sorted_kv_list:
                  top_k_trending_skills.append(skill[0])
            
        
            return {"topk":topk, "trending_skills": top_k_trending_skills},  HTTPStatus.OK
