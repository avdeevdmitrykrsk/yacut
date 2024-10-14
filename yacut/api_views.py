from flask import get_flashed_messages, jsonify, request

from . import app
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
    if urlmap:
        short_id = urlmap.short

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
    ), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_id_url(short_id):
    urlmap = URLMap.get_urlmap(short=short_id).first()
    if not urlmap:
        raise InvalidAPIUsage(
            message='Указанный id не найден',
            status_code=404
        )
    return jsonify(
        {
            "url": urlmap.original
        }
    ), 200
