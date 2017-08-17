# -*- coding:utf-8 -*-

from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime


class Site(Base):
    __tablename__ = 'mynews_sites'

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    url = Column(String(255), unique=True)
    category_id = Column(Integer)

    period = Column(Integer, default=10)
    state = Column(String(16), default='waiting')  # waiting, running
    rules = Column(Text)  # link extract rules, regular expression

    created_by = Column(Integer)

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    run_time = Column(DateTime, nullable=False, default=datetime.now)

    @classmethod
    def get_site_list(cls, page=1, per_page=20):
        return Site.query.paginate(page=page, per_page=per_page).items

    @classmethod
    def get_category_site_list(cls, category_id, page=1, per_page=20):
        return Site.query.filter_by(category_id = category_id).paginate(page=page, per_page=per_page).items
