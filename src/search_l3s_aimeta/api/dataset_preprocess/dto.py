from flask_restx import Model, fields



dto_task_preprocess_response_item = Model("DtoTaskPreprocessResponseItem",
                                        {
                                        "task_id" : fields.String(description='The task ID', example='10'),
                                        "task_title": fields.String(description='Title of the task', example='Schlitten [3_3]'),
                                        "text": fields.String(description='Processed text of the task', example='1. informieren Schlitten:  Arbeitsauftrag Sind deine Ziele ...  Lernfortschritt besser erkennen kannst.'),
                                        "tasksteps_ids": fields.List(fields.Integer, description="taskstep ids in the task", example= [23,24,25,26,27,28, 29]),
                                        "task_set_id" : fields.String(description="id of task set, corresponding to different owner/category", example= "2")
                                        }) 


dto_task_preprocess_response = Model('DtoTaskPreprocessResponse', 
                                     {
                                    'message': fields.String(required=True, example="success", description='Success message'),
                                     'results': fields.Nested( dto_task_preprocess_response_item, description='Results')
                                        })



dto_taskstep_preprocess_response_item = Model("DtoTaskStepPreprocessResponseItem",
                                        {
                                        "taskstep_id" : fields.String(description='The task step ID', example='23'),
                                        "taskstep_text": fields.String(description='Processed text of the task step', example='Arbeitsauftrag Sind deine Ziele festgelegt? ...  Deine persönliche Reflexion bitte in Notizen ablegen:'),
                                        }) 


dto_taskstep_preprocess_response = Model("DtoTaskStepPreprocessResponse",
                                        {
                                        'message': fields.String(required=True, example="success", description='Success message'), 
                                      'results': fields.Nested( dto_taskstep_preprocess_response_item, description='Results')
                                        })
