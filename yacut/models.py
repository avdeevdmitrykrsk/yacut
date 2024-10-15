import re
from datetime import datetime
from random import choices

from . import db
from .constants import (
    ATTEMPTS_STEP, CUSTOM_ID_REGEX_PATTERN, DEFAULT_SHORT_ID_LENGTH,
    DEFAULT_ATTEMPTS_COUNT, MAX_CUSTOM_ID_LENGTH, MAX_NUMBER_OF_ATTEMPTS,
    MSG_CANT_MAKE_ID, MSG_EMPTY_REQUEST_BODY, MSG_EXPECTED_FIELD_NOT_FOUND_URL,
    MSG_INVALID_SHORT_ID_NAME, MSG_SHORT_ID_ALREADY_EXIST,
    MAX_ORIGINAL_LINK_LENGTH, SHORT_ID_CHOICES
)
from .error_handlers import ValidationError


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_LINK_LENGTH))
    short = db.Column(db.String(MAX_CUSTOM_ID_LENGTH))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def get_urlmap(original=None, short=None):
        if short:
            return URLMap.query.filter_by(short=short)
        return URLMap.query.filter_by(original=original)

    @staticmethod
    def get_unique_short_id(
        original,
        length=DEFAULT_SHORT_ID_LENGTH,
        attempts_count=DEFAULT_ATTEMPTS_COUNT
    ):

        short = ''.join(choices(SHORT_ID_CHOICES, k=length))
        if URLMap.get_urlmap(short=short).first() is not None:
            attempts_count += ATTEMPTS_STEP

            if attempts_count >= MAX_NUMBER_OF_ATTEMPTS:
                raise ValidationError(MSG_CANT_MAKE_ID)
            URLMap.get_unique_short_id(original, attempt_count=attempts_count)
        return short

    @staticmethod
    def validate_and_make(data, api=False):

        if not api:
            data = {
                'url': data.original_link.data,
                'custom_id': data.custom_id.data
            }

        if data is None:
            raise ValidationError(MSG_EMPTY_REQUEST_BODY)
        if 'url' not in data:
            raise ValidationError(MSG_EXPECTED_FIELD_NOT_FOUND_URL)

        short = None
        original = data.get('url')

        if data.get('custom_id'):
            short = data.get('custom_id')
            if (
                len(short) > DEFAULT_SHORT_ID_LENGTH
                or not re.match(CUSTOM_ID_REGEX_PATTERN, short)
            ):
                raise ValidationError(MSG_INVALID_SHORT_ID_NAME)

            if URLMap.get_urlmap(short=short).first() is not None:
                raise ValidationError(MSG_SHORT_ID_ALREADY_EXIST)

        else:
            short = URLMap.get_unique_short_id(original)

        urlmap = URLMap.get_urlmap(original).first()
        if not urlmap:
            urlmap = URLMap(
                original=original,
                short=short.strip()
            )
            db.session.add(urlmap)
            db.session.commit()
        return urlmap
