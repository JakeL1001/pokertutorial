from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os
import logging
#imports necessary for functionality

pokerpack = Flask(__name__)
pokerpack.config.from_object(Config)
db = SQLAlchemy(pokerpack)
migrate = Migrate(pokerpack, db)
login = LoginManager(pokerpack)
login.login_view = "login"

from pokerapp import routes, models, errors

if not pokerpack.debug: #initializes the error logging funcitonality
    fileHandler = RotatingFileHandler("logs/pokererrors.log", maxBytes=20480, backupCount=5)
    fileHandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    fileHandler.setLevel(logging.INFO)
    pokerpack.logger.addHandler(fileHandler)
    
    pokerpack.logger.setLevel(logging.INFO)
    pokerpack.logger.info("Pokertutorial Startup")