# -*- coding:utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from mynews.models import Site
from mynews.forms import SiteForm


class Site(MethodView):

    def get(self, site_id):
        if site_id:
            site = Site.query.get(site_id)
            return site

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        sites = Site.get_category_site_list(page, per_page)
        return jsonify([site.to_dict() for site in sites])

    def post(self):
        form = SiteForm()
        form.create_api_json()
        site = form.create_site()
        return jsonify(site.to_dict()), 201

    def delete(self):
        pass

    def put(self):
        pass


class SiteNews(MethodView):

    def get(self, category_id):
        """/sites/site_id/news/"""
        pass