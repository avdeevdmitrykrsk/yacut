from flask import jsonify, render_template

from . import app
from .constants import HTTP_BAD_REQUEST, HTTP_NOT_FOUND


class InvalidAPIUsage(Exception):
    status_code = HTTP_BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


class ValidationError(InvalidAPIUsage):
    ...


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTP_NOT_FOUND)
def page_not_found(error):
    return render_template('404.html'), HTTP_NOT_FOUND
