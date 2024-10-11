from random import choices
from string import ascii_letters, digits

from flask import abort, flash, redirect, render_template, url_for, request

from . import app, db
from .forms import URLMapForm
from .models import URLMap

SHORT_ID_CHOICES = ascii_letters + digits
DEFAULT_SHORT_ID_LENGTH = 6


def get_unique_short_id(form, length=DEFAULT_SHORT_ID_LENGTH):
    unique_short_id = ''.join(choices(SHORT_ID_CHOICES, k=length))

    if form.custom_id.data:
        unique_short_id = form.custom_id.data

        if URLMap.query.filter_by(
            short=form.custom_id.data
        ).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)

    return f'http://{request.host}/{unique_short_id}'


def make_data_short_link(form, short_link):
    db.session.add(URLMap(original=form.original_link.data, short=short_link))
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    short_link = None
    form = URLMapForm()

    if form.validate_on_submit():
        urlmap = URLMap.query.filter_by(
            original=form.original_link.data
        ).first()

        short_link = get_unique_short_id(form)
        if urlmap is not None:
            short_link = urlmap.short
        make_data_short_link(form, short_link)

    return render_template('index.html', form=form, short_link=short_link)


@app.route('/<string:short_id>', methods=['GET'])
def short_id(short_id):
    short_link = URLMap.query.filter_by(
        short=f'http://{request.host}/{short_id}'
    ).first()
    print(short_link)
    return redirect(short_link)
