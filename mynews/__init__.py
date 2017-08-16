# -*- coding:utf-8 -*-

from flask import Flask
from mynews.exts import db


def init_app(app):
    db.init_app(app)


def register_app(app):
    pass


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)

    init_app(app)
    register_app(app)
    return app
