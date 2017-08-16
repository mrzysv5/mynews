# -*- coding:utf-8 -*-

from flask import json
from werkzeug.exceptions import HTTPException
from werkzeug._compat import text_type


class APIException(HTTPException):
    code = 400
    error = 'invalid request'

    def __init__(self, code=None, error=None, description=None, response=None):
        self.code = code or self.code
        self.error = error or self.error
        super(APIException, self).__init__(description, response)

    def get_body(self, environ=None):
        return text_type(json.dumps(dict(
            error=self.error,
            msg=self.description
        )))

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class FormError(APIException):
    error = 'invalid form data'

    def __init__(self, form, response=None):
        self.form = form
        super(FormError, self).__init__(None, response)

    def get_body(self, environ=None):
        return text_type(json.dumps(dict(
            error=self.error,
            msg=self.form.errors
        )))
