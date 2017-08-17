# -*- coding:utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from mynews.models import Category, Site, News
from mynews.forms import CategoryForm, SiteForm
from mynews.errors import APIException


class CategoryAPI(MethodView):

    def get(self, category_id):
        if category_id:
            category = Category.query.get(category_id)
            return jsonify(category)

        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories])

    def post(self):
        form = CategoryForm.create_api_json()
        category = form.create_category()
        return jsonify(category.to_dict()), 201

    def delete(self):
        pass

    def put(self):
        pass


class CategorySiteAPI(MethodView):

    def get(self, category_id, site_id):
        """/categories/category_id/site/"""
        if site_id:
            site = Site.query.get(site_id)
            if site is None:
                raise APIException(
                    code=404,
                    error='site id is not found'
                )
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        sites = Site.get_category_site_list(category_id, page, per_page)
        return jsonify([site.to_dict() for site in sites.items])

    def post(self, category_id):
        form = SiteForm()
        form.create_api_json()
        if category_id != form.category_id.data:
            raise APIException(
                code=400,
                error='category is not equal'
            )
        site = form.create_site()
        return jsonify(site.to_dict()), 201



class CategoryNews(MethodView):

    def get(self, category_id):
        """/categories/category_id/news/"""
        pass
