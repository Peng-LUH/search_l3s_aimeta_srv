from flask_restx import Model, fields

dto_summary_response = Model("DtoSummaryResponse", {
    "task_id": fields.String(description='The task ID', example='10'),
    "summary": fields.String(description='Summary of the given task', example="This is the summary of the task.")
})

