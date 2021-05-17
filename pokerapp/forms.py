from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.fields.core import FloatField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from pokerapp.models import User

class LoginForm(FlaskForm): #form for logging in existing users
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")
    
class RegistrationForm(FlaskForm): #form for registering new users
    username = StringField("Username", validators = [DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
    
    def validate_username(self, username): #ensures unique username, cant register username if it already exists
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("That username is taken")
    
    def validate_email(self, email): #ensures unique email, cant register email if it already is used
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("This email address alredy exists")
        
class QuizForm(FlaskForm): #form for submitting quiz results to the database
    id = IntegerField("User ID")
    score = FloatField("Score")
    submit2 = SubmitField("Submit and Continue")
        