from http import HTTPStatus
from flask_restx import Namespace, Resource

ns_test = Namespace("test", validate=True)

@ns_test.route("/aimeta-test", endpoint="aimeta_test")
class AimetaTest(Resource):
    def get(self):
        return {"message": "Success"}