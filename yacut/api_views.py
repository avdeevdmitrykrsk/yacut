from flask import get_flashed_messages, jsonify, request

from . import app
from .constants import HTTP_CREATED, HTTP_NOT_FOUND, HTTP_OK
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def make_short_id():
    data = request.get_json(silent=True)
    host = f'{request.scheme}://{request.host}'
    short_id = None

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if data.get('custom_id'):
        short_id = data.get('custom_id')

    urlmap = URLMap.validate_and_make(data.get('url'), short_id)

    flashed_message = get_flashed_messages()
    if flashed_message:
        raise InvalidAPIUsage(
            message=flashed_message.pop(),
        )

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
            message='Указанный id не найден',
            status_code=HTTP_NOT_FOUND
        )
    return jsonify(
        {
            "url": urlmap.original
        }
    ), HTTP_OK
