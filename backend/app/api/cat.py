"""cats endpoints"""

from flask_restx import Namespace, Resource, fields

cat_api = Namespace("cats", description="Cats related operations")

cat = cat_api.model(
    "Cat",
    {
        "id": fields.String(required=True, description="The cat identifier"),
        "name": fields.String(required=True, description="The cat name"),
    },
)

CATS = [
    {"id": "felix", "name": "Felix"},
]


@cat_api.route("/")
class CatList(Resource):
    """_summary_

    Args:
        Resource (class): RestX Resource class

    Returns:
        CATS (list): A list of cats
    """
    @cat_api.doc("list_cats")
    @cat_api.marshal_list_with(cat)
    def get(self):
        """List all cats"""
        return CATS


@cat_api.route("/<id>")
@cat_api.param("id", "The cat identifier")
@cat_api.response(404, "Cat not found")
class Cat(Resource):
    """_summary_

    Args:
        Resource (class): RestX Resource class

    Returns:
        CATS (dict): A list of cats
    """
    @cat_api.doc("get_cat")
    @cat_api.marshal_with(cat)
    def get(self, id):
        """Fetch a cat given its identifier"""
        for cat in CATS:
            if cat["id"] == id:
                return cat
        cat_api.abort(404)
