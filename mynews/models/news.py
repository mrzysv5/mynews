# -*- coding:utf-8 -*-

from .base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


class News(Base):
    __tablename__ = 'mynews_news'

    id = Column(Integer, primary_key=True)

    title = Column(String(125))
    url = Column(String(255), unique=True)

    site_id = Column(Integer)
    category_id = Column(Integer)

    created_at = Column(DateTime, nullable=False, default=datetime.now)

    @classmethod
    def get_news_list(cls, page=1, per_page=20):
        return News.query.paginate(page, per_page).items