from flask import get_flashed_messages, jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id, make_data_short_link


@app.route('/api/id/', methods=['POST'])
def make_short_id():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    host = f'{request.scheme}://{request.host}'
    short_id = data.get('custom_id')
    short_id = get_unique_short_id(unique_short_id=short_id)

    flashed_message = get_flashed_messages()
    if flashed_message:
        raise InvalidAPIUsage(
            message=flashed_message.pop(),
        )

    urlmap = make_data_short_link(data['url'], short_id)
    response = jsonify(
        {
            "url": urlmap.original,
            "short_link": f'{host}/{urlmap.short}'
        }
    ), 201
    return response


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_short_id_url(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
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
