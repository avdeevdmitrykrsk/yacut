from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import (
    CUSTOM_ID_REGEX_PATTERN,
    INFO_FORM_ENTER_LONG_LINK,
    INFO_FORM_MAKE,
    INFO_FORM_YOUR_LONG_LINK_OPTION,
    MAX_CUSTOM_ID_LENGTH, MAX_ORIGINAL_LINK_LENGTH,
    MIN_CUSTOM_ID_LENGTH, MIN_ORIGINAL_LINK_LENGTH,
    MSG_FIELD_REQUIRED
)


class URLMapForm(FlaskForm):
    original_link = URLField(
        INFO_FORM_ENTER_LONG_LINK,
        validators=[
            DataRequired(message=MSG_FIELD_REQUIRED),
            Length(
                MIN_ORIGINAL_LINK_LENGTH,
                MAX_ORIGINAL_LINK_LENGTH
            )
        ]
    )
    custom_id = TextAreaField(
        INFO_FORM_YOUR_LONG_LINK_OPTION,
        validators=[
            Length(
                MIN_CUSTOM_ID_LENGTH,
                MAX_CUSTOM_ID_LENGTH
            ),
            Regexp(CUSTOM_ID_REGEX_PATTERN),
            Optional()
        ]
    )
    submit = SubmitField(INFO_FORM_MAKE)
