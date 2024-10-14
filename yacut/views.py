from flask import redirect, render_template, request

from . import app
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index():
    short_id = None
    host = f'{request.scheme}://{request.host}'
    form = URLMapForm()

    if form.validate_on_submit():
        if form.custom_id.data:
            short_id = form.custom_id.data
        urlmap = URLMap.validate_and_make(form.original_link.data, short_id)
        if urlmap:
            short_id = urlmap.short

    return render_template(
        'index.html', form=form, short_id=short_id, host=host
    )


@app.route('/<string:short_id>')
def redirect_to_original_link(short_id):
    return redirect(URLMap.get_urlmap(short=short_id).first_or_404().original)
