from flask import abort, redirect, render_template, request

from . import app
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id, make_data_short_link


@app.route('/', methods=['GET', 'POST'])
def index():
    short_id = None
    host = f'{request.scheme}://{request.host}'
    form = URLMapForm()

    if form.validate_on_submit():
        original_link = form.original_link.data
        urlmap = URLMap.query.filter_by(
            original=original_link
        ).first()

        if form.custom_id.data:
            short_id = form.custom_id.data
        short_id = get_unique_short_id(short_id)
        if urlmap is not None:
            short_id = urlmap.short

        make_data_short_link(original_link, short_id)

    return render_template(
        'index.html', form=form, short_id=short_id, host=host
    )


@app.route('/<string:short_id>')
def redirect_to_original_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if not urlmap:
        abort(404)
    return redirect(urlmap.original)
