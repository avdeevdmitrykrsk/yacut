from datetime import datetime

from . import db
from .constants import MAX_CUSTOM_ID_LENGTH, MAX_ORIGINAL_LINK_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_LINK_LENGTH))
    short = db.Column(db.String(MAX_CUSTOM_ID_LENGTH))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def get_original_link(short):
        return URLMap.query.filter_by(short=short)
