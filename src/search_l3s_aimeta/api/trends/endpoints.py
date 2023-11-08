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

parser = ns_trends.parser()
parser.add_argument('loc', type=str, required=True, help='location for searching job', default="berlin")
parser.add_argument('job_name', type=str, required=True,help="job name", default="machine learning")
parser.add_argument('radius', type=int, required=False, help='radius for searching jobs', default=5)



@ns_trends.route("/search-jobs/", endpoint="search-jobs")
class SearchJobs(Resource):   
    @ns_trends.marshal_list_with(dto_jobs_search_response)

    @ns_trends.expect(parser)
    def get(self):   
            "Search for job offers"

            args = parser.parse_args()
            loc, job_name, radius = args['loc'], args['job_name'], args['radius']

            assert radius>=0, abort(400, "Invalid radius, please try again with non-negative radius.")


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
    @ns_trends.expect(parser)
    def get(self):   
            "get skills"    

            args = parser.parse_args()
            loc, job_name, radius = args['loc'], args['job_name'], args['radius']        
            # loc = request.args.get('loc')
            # job_name = request.args.get('job_name')
            # radius = request.args.get('radius')

            assert radius>=0, abort(400, "Invalid radius, please try again with non-negative radius.")


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
    


parser_trends = ns_trends.parser()
parser_trends.add_argument('loc', type=str, required=True, help='location for searching job', default="berlin")
parser_trends.add_argument('job_name', type=str, required=True,help="job name", default="machine learning")
parser_trends.add_argument('radius', type=int, required=False, help='radius for searching jobs', default=5)
parser_trends.add_argument('topk', type=int, required=True, help='top k trending skills', default=5)


@ns_trends.route("/trending-skills/", endpoint="trending-skills")
class GetTrends(Resource):   
    @ns_trends.marshal_with(dto_trending_skills_response)  
    @ns_trends.expect(parser_trends)
    def get(self):   
            "get trending skills"     

            args = parser_trends.parse_args()
            loc, job_name, radius, topk = args['loc'], args['job_name'], args['radius'], args['topk']

            assert radius>=0, abort(400, "Invalid radius, please try again with 0 or greater radius.")     
            
            assert topk>0, abort(400, "Invalid topk. Please use topk greater than 0.")     


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
