from flask_jsonpify import jsonpify
from flask import Blueprint, request, Response
from . import controllers


def make_blueprint():
    """Create blueprint.
    """

    # Create instance
    blueprint = Blueprint('resolve', 'resolve')

    # Controller proxies
    def resolver():
        path = request.values.get('path')
        try:
            return jsonpify(controllers.resolve(path))
        except Exception as e:
            return Response(str(e), status=400)

    # Register routes
    blueprint.add_url_rule(
            'resolve', 'resolve', resolver, methods=['GET'])

    # Return blueprint
    return blueprint
