# -*- coding:utf-8 -*-

from flask.views import MethodView
from flask import request, jsonify

from mynews.models import News
from mynews.forms import NewsForm


class NewsAPI(MethodView):

    def get(self, news_id):
        if news_id:
            news = News.query.get(news_id)
            return jsonify(news.to_dict())

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        news_list = News.get_news_list(page, per_page)
        return jsonify([news.to_dict() for news in news_list])

    def post(self):
        form = NewsForm()
        form.create_api_json()
        news = form.create_news()
        return jsonify(news.to_dict()), 201

    def delete(self):
        pass

    def put(self):
        pass
