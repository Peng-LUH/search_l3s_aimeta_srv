from flask_restx import Model, fields


dto_task_preprocess_response = Model("DtoTaskPreprocessResponse",
                                        {
                                        "task_id" : fields.String(description='The task ID', example='10'),
                                        "task_title": fields.String(description='Title of the task', example='Schlitten [3_3]'),
                                        "text": fields.String(description='Processed text of the task', example='1. informieren Schlitten:  Arbeitsauftrag Sind deine Ziele ...  Lernfortschritt besser erkennen kannst.'),
                                        "tasksteps_ids": fields.List(fields.Integer, description="taskstep ids in the task", example= [23,24,25,26,27,28, 29]),
                                        "task_set_id" : fields.String(description="id of task set, corresponding to different owner/category", example= "2")
                                        }) 

dto_taskstep_preprocess_response = Model("DtoTaskStepPreprocessResponse",
                                        {
                                        "taskstep_id" : fields.String(description='The task step ID', example='23'),
                                        "taskstep_text": fields.String(description='Processed text of the task step', example='Arbeitsauftrag Sind deine Ziele festgelegt? ...  Deine persönliche Reflexion bitte in Notizen ablegen:'),
                                        }) 