# -*- coding:utf-8 -*-

from mynews.exts import db


class BaseMixin(object):
    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        data = {}
        for key in self.__mapper__.c.keys():
            data[key] = getattr(self, key)
        return data


class Base(db.Model, BaseMixin):
    __abstract__ = True
