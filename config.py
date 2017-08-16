# -*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

print('basedir....')
print(basedir)


class Config(object):
    SECRET_KEY = 'REPLACE ME'


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    FLASKY_MAIL_SUBJECT_PREFIX = 'Notice'
    FLASKY_MAIL_SENDER = 'mrzysv5@sina.com'
    MAIL_SERVER = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class ProdConfig(Config):
    ENV = 'prod'
    FLASKY_MAIL_SUBJECT_PREFIX = '通知'
    FLASKY_MAIL_SENDER = 'admin@mail.mr-zys.top'
    MAIL_SERVER = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

