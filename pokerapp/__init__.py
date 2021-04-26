from flask import Flask
from config import Config

pokerpack = Flask(__name__)
pokerpack.config.from_object(Config)

from pokerapp import routes