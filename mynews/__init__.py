# -*- coding:utf-8 -*-

from flask import Flask
from mynews.exts import db


def init_app(app):
    db.init_app(app)


def register_api(app, view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])


def register_app(app):
    from mynews.api import CategoryAPI, CategorySiteAPI, NewsAPI
    register_api(
        app,
        CategoryAPI,
        'categories_api',
        '/api/categories',
        pk='category_id'
    )
    register_api(
        app,
        CategorySiteAPI,
        'categories_sites_api',
        '/api/categories/<int:category_id>/site',
        pk='site_id'
    )
    register_api(
        app,
        NewsAPI,
        'news_api',
        '/api/news',
        pk='news_id'
    )


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)

    init_app(app)
    register_app(app)
    print(app.url_map)
    print(db)
    return app
