from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import handle_errors
from src.validators.tag_creator_validator import validate_tag

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    response = None
    try:
        validate_tag(request)
        http_req = HttpRequest(body=request.json)
        response = TagCreatorView().validate_and_create(http_req)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.status_code, response.body)
