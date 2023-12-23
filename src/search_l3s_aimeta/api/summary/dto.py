from flask_restx import Model, fields

dto_summary_response_item = Model("DtoSummaryResponseItem", {
    "task_id": fields.String(description='The task ID', example='10'),
    "summary": fields.String(description='Summary of the given task', example="""In dieser Lerneinheit steht der Schlitten im Fokus. 
                             Du wirst lernen, deine Ziele zu definieren, 
                             die Funktion des Bauteils zu verstehen und einen genauen Arbeitsplan zu erstellen. 
                             Dabei ist es wichtig, Form- und Lagetoleranzen einzuhalten und Sicherheitsvorschriften zu beachten. 
                             Nachdem du den Schlitten hergestellt hast, 
                             kannst du deine Arbeit reflektieren und deine Ergebnisse mit deinem Lernbegleiter besprechen. 
                             Um deine Fortschritte festzuhalten, füllst du die \"Ich kann ...\"-Listen für überfachliche und fachliche Kompetenzen aus. 
                             Lade deine Ergebnisse in deine Notizen hoch. 
                             Ganz wichtig: 
                             Du kannst die bereits heruntergeladenen Listen und Bewertungsbögen weiterbearbeiten und musst keine neuen anlegen, 
                             um deinen Lernfortschritt besser nachverfolgen zu können. 
                             Diese Lerneinheit ist eine spannende Herausforderung für dich, 
                             also plane und arbeite sorgfältig und effektiv, um den Schlitten in optimaler Qualität herzustellen. Viel Erfolg!""")
                        })



dto_summary_response = Model('DtoSummaryResponse',  {
                            'message': fields.String(required=True, example="success", description='Success message'),
                            'results': fields.Nested( dto_summary_response_item, description='Results')
                                        })
