import re
from datetime import datetime
from flask import flash
from random import choices

from . import db
from .constants import (
    CUSTOM_ID_REGEX_PATTERN, DEFAULT_SHORT_ID_LENGTH, MAX_CUSTOM_ID_LENGTH,
    MAX_ORIGINAL_LINK_LENGTH, SHORT_ID_CHOICES
)
from .error_handlers import InvalidAPIUsage


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
    def get_unique_short_id(original, length=DEFAULT_SHORT_ID_LENGTH):
        urlmap = URLMap.get_urlmap(original).first()
        if urlmap is not None:
            return urlmap.short

        short = ''.join(choices(SHORT_ID_CHOICES, k=length))
        if URLMap.get_urlmap(short=short).first() is not None:
            URLMap.get_unique_short_id(original)  # Опасно!
        return short

    @staticmethod
    def validate_and_make(original, short):
        if short:
            print(short)
            if (
                len(short) > DEFAULT_SHORT_ID_LENGTH
                or not re.match(CUSTOM_ID_REGEX_PATTERN, short)
            ):
                raise InvalidAPIUsage(
                    'Указано недопустимое имя для короткой ссылки'
                )

            if URLMap.get_urlmap(short=short).first() is not None:
                flash('Предложенный вариант короткой ссылки уже существует.')
                return None
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
