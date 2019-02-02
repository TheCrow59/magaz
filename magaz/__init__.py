from flask import Flask, redirect, Response
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

app.config.from_object('magaz.config.Config')
app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from magaz.models.entity import Category, Product, Ticket, Basket


basic_auth = BasicAuth(app)

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

class MyModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


admin = Admin(app, name='magaz', template_mode='bootstarp3')
admin.add_view(MyModelView(Category, db.session))
admin.add_view(MyModelView(Product, db.session))
admin.add_view(MyModelView(Ticket, db.session))
admin.add_view(MyModelView(Basket, db.session))
