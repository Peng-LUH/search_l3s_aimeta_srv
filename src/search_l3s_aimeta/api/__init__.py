"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api
import sys


sys.path.append("..")


api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
# authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="0.0.1",
          title="L3S AI-Meta Service(AIMS) for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
          doc="/ui",
        #   authorizations=authorizations,
          )

from search_l3s_aimeta.api.test.endpoints import ns_test
from search_l3s_aimeta.api.dataset_utils.endpoints import ns_dataset_generator
from search_l3s_aimeta.api.dataset_preprocess.endpoints import ns_dataset_preprocess
from search_l3s_aimeta.api.summary.endpoints import ns_summary
from search_l3s_aimeta.api.content_keywords.endpoints import ns_content_keywords
from search_l3s_aimeta.api.context_keywords.endpoints import ns_context_keywords
from search_l3s_aimeta.api.learning_goal.endpoints import ns_learning_goal
from search_l3s_aimeta.api.quiz.endpoints import ns_quiz
from search_l3s_aimeta.api.title.endpoints import ns_title
from search_l3s_aimeta.api.trends.endpoints import ns_trends


api.add_namespace(ns_test, path="/aims")
api.add_namespace(ns_dataset_generator, path="/aims")
api.add_namespace(ns_dataset_preprocess, path='/aims')
api.add_namespace(ns_summary, path='/aims')
api.add_namespace(ns_content_keywords, path='/aims')
api.add_namespace(ns_context_keywords, path='/aims')
api.add_namespace(ns_learning_goal, path='/aims')
api.add_namespace(ns_quiz, path='/aims')
api.add_namespace(ns_title, path='/aims')
api.add_namespace(ns_trends, path='/aims')









