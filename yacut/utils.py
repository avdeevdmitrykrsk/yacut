from random import choices

from flask import flash, render_template, jsonify

from . import db
from .constants import (
    SHORT_ID_CHOICES, DEFAULT_SHORT_ID_LENGTH,
    MAX_SHORT_ID_LENGTH, PREFIX
)
from .constants import UNSUPPORTED_LETTERS
from .error_handlers import InvalidAPIUsage
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id(
        unique_short_id=None, length=DEFAULT_SHORT_ID_LENGTH, api=False
):
    if not unique_short_id:
        unique_short_id = ''.join(choices(SHORT_ID_CHOICES, k=length))
    if URLMap.query.filter_by(
        short=unique_short_id
    ).first() is not None:
        flash('Предложенный вариант короткой ссылки уже существует.')
        return None
    return unique_short_id


def make_data_short_link(original_link, short_link):

    if (
        len(short_link) > MAX_SHORT_ID_LENGTH
        or any([x for x in short_link if x in UNSUPPORTED_LETTERS])
    ):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки'
        )

    urlmap = URLMap.query.filter_by(original=original_link).first()
    if not urlmap:
        urlmap = URLMap(
            original=original_link,
            short=short_link.strip()
        )
        db.session.add(urlmap)
        db.session.commit()
    return urlmap
