from flask_restx import Model, fields


dto_taught_skills_response = Model("DtoTaughtSkillsResponse", {
    "task_id": fields.String(description='The task ID', example='10'),
    "new_skills": fields.List(fields.String, description='List of skills taught in the learning task', example=[
    "X",
    "Y",
    "Z"
  ])
})

dto_existing_skills_response = Model("DtoExistingSkillsResponse", {
    "task_id": fields.String(description='The task ID', example='10'),
    "existing_skills": fields.List(fields.String, description='List of existing skills in MLS for the learning task', example=[
    "A",
    "B",
    "C"
  ])
})

