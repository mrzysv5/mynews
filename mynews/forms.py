
# -*- coding:utf-8 -*-
from flask import request
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Email, DataRequired, EqualTo, StopValidation, ValidationError, URL, NumberRange
from werkzeug.datastructures import MultiDict

from mynews.errors import FormError
from mynews.models import Category
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
            raise StopValidation('username %s has been registered.' % field.data)

    def create_category(self):
        category = Category(name=self.name.data)
        try:
            db.session.add(category)
            db.session.commit(category)
        except Exception as e:
            db.session.rollback()
        return category