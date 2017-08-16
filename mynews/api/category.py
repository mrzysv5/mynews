# -*- coding:utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from mynews.models import Category
from mynews.forms import CategoryForm


class Category(MethodView):

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


class CategoryNews(MethodView):

    def get(self, category_id):
        """/categories/category_id/news/"""
        pass
