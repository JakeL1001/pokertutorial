from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

pokerpack = Flask(__name__)
pokerpack.config.from_object(Config)
db = SQLAlchemy(pokerpack)
migrate = Migrate(pokerpack, db)
login = LoginManager(pokerpack)
login.login_view = "login"

from pokerapp import routes, models