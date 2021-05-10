# pylint: disable=no-member

from datetime import datetime
from pokerapp import db
from pokerapp import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Results(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    quiz1 = db.Column(db.Float)
    quiz2 = db.Column(db.Float)
    quiz3 = db.Column(db.Float)
    total = db.Column(db.Float)
    
    def __repr__(self):
        return '<Results {}>'.format(self.quiz1)
