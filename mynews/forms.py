
# -*- coding:utf-8 -*-
from flask import request
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField
from wtforms.validators import Email, DataRequired, EqualTo, StopValidation, ValidationError, URL, NumberRange
from werkzeug.datastructures import MultiDict

from mynews.errors import FormError
from mynews.models import Category, Site, News
from mynews.exts import db


class BaseForm(Form):
    @classmethod
    def create_api_json(cls, obj=None):
        formdata = MultiDict(request.get_json())
        form = cls(formdata=formdata, obj=obj, csrf_enabled=False)
        if not form.validate():
            raise FormError(form)
        return form


class CategoryForm(BaseForm):
    name = StringField(label='分类名称', validators=[DataRequired()])

    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise StopValidation('分类名 %s 已经被使用了' % field.data)

    def create_category(self):
        category = Category(name=self.name.data)
        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return category


class SiteForm(BaseForm):
    title = StringField(label='站点标题', validators=[DataRequired()])
    url = StringField(label='站点链接', validators=[DataRequired(), URL()])
    category_id = IntegerField(label='分类ID', validators=[])
    period = IntegerField(
        label="抓取周期（分钟）",
        validators=[NumberRange(min=1, max=60, message="抓取周期需要在1到60分钟之间")])
    rules = StringField(label="提取规则", validators=[DataRequired()])

    def validate_url(self, field):
        if Site.query.filter_by(url=field.data).first():
            raise StopValidation('url %s 已经被添加了' % field.data)
        return True

    def validate_title(self, field):
        if Site.query.filter_by(title=field.data).first():
            raise StopValidation('title %s 已经被使用了' % field.data)
        return True

    def create_site(self):
        site = Site(
            title=self.title.data,
            url=self.url.data,
            period=self.period.data * 60,
            rules=self.rules.data,
            created_by=1
        )
        try:
            db.session.add(site)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return site


class NewsForm(BaseForm):
    title = StringField(label="新闻标题", validators=[DataRequired()])
    url = StringField(label="新闻链接", validators=[DataRequired(), URL()])
    site_id = IntegerField(label="所属站点分类", validators=[DataRequired()])
    created_at = DateField(label="创建时间", format="%Y-%m-%d %H:%M:%s")

    def validate_title(self, field):
        if News.query.filter_by(title=field.data):
            raise StopValidation('新闻标题 %s 已经被使用了' % field.data)
        return True

    def validate_url(self, field):
        if News.query.filter_by(url=field.data):
            raise StopValidation('新闻链接 %s 已经被使用了' % field.data)
        return True

    def create_news(self):
        site = Site.query.get(self.site_id.data)
        category_id = site.category_id
        news = News(
            title=self.title.data,
            url=self.url.data,
            site_id=self.site_id.data,
            created_at=self.created_at.data,
            category_id=category_id
        )
        try:
            db.session.add(news)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        return news