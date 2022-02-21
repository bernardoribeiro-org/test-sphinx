"""simple restx api initialize"""
from flask_restx import Api

from .cat import cat_api
from .dog import dog_api

flask_api = Api(
    title="Zoo API",
    version="1.0",
    description="A simple demo API",
    docs='swagger'
)
"""creates flask api"""

flask_api.add_namespace(cat_api)
""" add cat namespace"""
flask_api.add_namespace(dog_api)
""" add dog namespace"""
