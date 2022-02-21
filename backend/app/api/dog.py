"""Dogs endpoints"""

from flask_restx import Namespace, Resource, fields

dog_api = Namespace("dogs", description="Dogs related operations")

dog = dog_api.model(
    "Dog",
    {
        "id": fields.String(required=True, description="The dog identifier"),
        "name": fields.String(required=True, description="The dog name"),
    },
)

DOGS = [
    {"id": "medor", "name": "Medor"},
]


@dog_api.route("/")
class DogList(Resource):
    """defines Dog list endpoint"""
    @dog_api.doc("list_dogs")
    @dog_api.marshal_list_with(dog)
    def get(self):
        """List all dogs"""
        return DOGS


@dog_api.route("/<id>")
@dog_api.param("id", "The dog identifier")
@dog_api.response(404, "Dog not found")
class Dog(Resource):
    """defines Dog GET by id endpoint"""
    @dog_api.doc("get_dog")
    @dog_api.marshal_with(dog)
    def get(self, id):
        """Fetch a dog given its identifier"""
        for dog in DOGS:
            if dog["id"] == id:
                return dog
        dog_api.abort(404)
