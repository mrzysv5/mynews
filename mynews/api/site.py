# -*- coding:utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from mynews.models import Site, News
from mynews.forms import SiteForm, SiteEditForm


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

    def put(self, site_id):
        form = SiteEditForm()
        form.create_api_json()
        form.update(site_id)
        return jsonify({'msg': '更新成功'})


class SiteNews(MethodView):

    def get(self, site_id, news_id):
        """/sites/<int:site_id>/news/"""
        if news_id:
            news = News.query.get(news_id)
            return jsonify(news.to_dict())

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        news_list = News.get_news_list(page, per_page)
        return jsonify([news.to_dict() for news in news_list])