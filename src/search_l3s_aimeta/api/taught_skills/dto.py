from flask_restx import Model, fields


dto_new_existing_skills_response_item = Model("DtoNewExistingSkillsResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "new_skills": fields.List(fields.String, description='List of new skills in the learning task', example=                            
                                                                        [
                                                                          "Zielsetzung und Selbstreflexion",
                                                                          "Effektive Planung",
                                                                          "Praktische Umsetzung",
                                                                          "Beobachtung und Reflexion",
                                                                          "Erfolgskontrolle"
                                                                        ]),
    "existing_skills": fields.List(fields.String, description='List of existing skills ids for the learning task', example=[
    "1",
    "2",
    "3"])                                                              

})



dto_new_existing_skills_response = Model('DtoNewExistingSkillsResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested(dto_new_existing_skills_response_item, description='Results')
                                        })
