# -*- coding:utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify


class Site(MethodView):

    def get(self, site_id):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


class SiteNews(MethodView):

    def get(self, category_id):
        """/sites/site_id/news/"""
        pass