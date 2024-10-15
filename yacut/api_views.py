from flask import jsonify, request

from . import app
from .constants import (
    HTTP_CREATED, HTTP_NOT_FOUND, HTTP_OK, MSG_SHORT_ID_NOT_FOUND
)
from .error_handlers import InvalidAPIUsage, ValidationError
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def make_short_id():
    data = request.get_json(silent=True)
    host = f'{request.scheme}://{request.host}'

    try:
        urlmap = URLMap.validate_and_make(data, api=True)
    except ValidationError as error:
        raise InvalidAPIUsage(error.message)

    return jsonify(
        {
            "url": urlmap.original,
            "short_link": (
                f'{host}/'
                f'{urlmap.short}'
            )
        }
    ), HTTP_CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_id_url(short_id):
    urlmap = URLMap.get_urlmap(short=short_id).first()
    if not urlmap:
        raise InvalidAPIUsage(
            message=MSG_SHORT_ID_NOT_FOUND,
            status_code=HTTP_NOT_FOUND
        )
    return jsonify(
        {
            "url": urlmap.original
        }
    ), HTTP_OK
