from flask_restx import Model, fields

parameter_model = Model("Parameter", {
    "parameter_name": fields.String(description="mls-api parameter")
})

dataset_model = Model("Mls_Dataset", {
    "name": fields.String(description="description: dataset name, e.g., tasks, documents"),
    "parameters": fields.List(fields.Nested(parameter_model), description="List of mls-api parameters"),
})

object_model = Model("Mls_Object", {
    "object_id": fields.String
})

input_dataset_model = Model("Dataset", {
    "dataset_name": fields.String(required=True),
})



