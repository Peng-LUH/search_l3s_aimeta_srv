from flask_restx import Model, fields


dto_jobs_search_request = Model("DtoJobsSearchRequest", {
    "loc": fields.String(description="location for searching jobs", default=None, required=True),
    "job_name": fields.String(description="job name", default=None),
    "radius": fields.String(description="radius in which we are searching jobs", default=50)
})

dto_skills_request = Model("DtoSkillsRequest", {
    "loc": fields.String(),
    "job_name": fields.String(),
    "radius": fields.Integer()
})

dto_trending_skills_request = Model("DtoTrendingSkillsRequest", {
    "loc": fields.String(),
    "job_name": fields.String(),
    "radius": fields.Integer()
})



dto_jobs_search_response = Model("DtoJobsSearchResponse", {
    "job_offers": fields.List(fields.Raw(description="List of Dictionaries"))
})


dto_skills_response = Model("DtoSkillsResponse", {
    "skills": fields.Raw(description="required skills with auspraegungen (skill level and skill name) and hierarchieName(context) for the given job.")
})



dto_trending_skills_response = Model("DtoTrendingSkillsResponse", {
    "topk": fields.String(description='number of top Trending Skills', example=5),
    "trending_skills": fields.List(fields.String, description='List of Trending Skills', example=["Kundenberatung, -betreuung",
    "Abrechnung",
    "Kosten- und Leistungsrechnung",
    "Akquisition",
    "Korrespondenz"])
})



