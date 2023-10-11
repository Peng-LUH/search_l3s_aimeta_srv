from flask_restx import Model, fields

dto_summary_response = Model("DtoSummaryResponse", {
    "unit_id": fields.String(),
    "summary": fields.String()
})

