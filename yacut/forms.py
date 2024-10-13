from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import (
    CUSTOM_ID_REGEX_PATTERN,
    MAX_CUSTOM_ID_LENGTH, MAX_ORIGINAL_LINK_LENGTH,
    MIN_CUSTOM_ID_LENGTH, MIN_ORIGINAL_LINK_LENGTH
)


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(
                MIN_ORIGINAL_LINK_LENGTH,
                MAX_ORIGINAL_LINK_LENGTH
            )
        ]
    )
    custom_id = TextAreaField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                MIN_CUSTOM_ID_LENGTH,
                MAX_CUSTOM_ID_LENGTH
            ),
            Regexp(CUSTOM_ID_REGEX_PATTERN),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
