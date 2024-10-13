from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='../html/css'
)
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, models, views
