import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')  # required for quasar
app = Flask(__name__, static_folder=static_dir, template_folder=static_dir)      # as we server dynamic js all is static

# DEVELOPMENT AND PRODUCTION
app.config.from_object('app.cfg.DevelopmentConfig')
# app.config.from_object('app.cfg.ProductionConfig')

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Extensions > Needs to come after app/db creation
# as these modules need the app/db
from app.extensions import auth_praeto

# Routes and models > needs to come even later to use
# decorators etc.
from app import routes, models
