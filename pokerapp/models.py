# pylint: disable=no-member

from datetime import datetime
from pokerapp import db
from pokerapp import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model): #User records schema for the database
    id = db.Column(db.Integer, primary_key=True) #unique IDs for each user
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128)) #password is saved as hash for security

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, pword): #generates password hash from password, and stores it
        self.password_hash = generate_password_hash(pword)
    
    def check_password(self, pword): #checks the password against the existing hash, used for login
        return check_password_hash(self.password_hash, pword)
    
class Results(db.Model): #Results records schema, user_id is foreign key to the id field from user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, unique=True)
    quiz1 = db.Column(db.Float) #stores each quiz results, used for restricting access to other quizzes
    quiz2 = db.Column(db.Float)
    quiz3 = db.Column(db.Float)
    finalquiz = db.Column(db.Float)
    
    def __repr__(self):
        return '<Results {}>'.format(self.quiz1)
