"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api


api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="1.0",
          title="L3S AI-Meta Service for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
          doc="/ui",
          authorizations=authorizations,
          )

# from search_l3s_search_srv.api.simple_search_srv.endpoints import ns_simple_search
# api.add_namespace(ns_simple_search, path="/simple-search-srv")

