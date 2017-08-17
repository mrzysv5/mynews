# -*- coding:utf-8 -*-

from .base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from mynews.exts import db

class Category(Base):
    __tablename__ = 'mynews_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    created_at = Column(DateTime, nullable=False, default=datetime.now)

    def remove(self):
        flag = True
        try:
            db.session.remove(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flag = False
        return flag

