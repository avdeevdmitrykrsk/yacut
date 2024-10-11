from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 256)
        ]
    )
    custom_id = TextAreaField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16), Optional()
        ]
    )
    submit = SubmitField('Создать')
