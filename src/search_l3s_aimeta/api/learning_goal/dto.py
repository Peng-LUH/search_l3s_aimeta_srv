from flask_restx import Model, fields

dto_learning_goal_response = Model("DtoLearningGoalResponse", {
    "unit_id": fields.String(),
    "learning_goal": fields.List(fields.String())
})

