from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from pokerapp.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")
    
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("That username is taken")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("This email address alredy exists")
        
class QuizForm1(FlaskForm): #make all data required
    question_1 = RadioField(u"Favorite Breakfast Meat1", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_2 = RadioField(u"Favorite Breakfast Meat2", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_3 = RadioField(u"Favorite Breakfast Meat3", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_4 = RadioField(u"Favorite Breakfast Meat4", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_5 = RadioField(u"Favorite Breakfast Meat5", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    submit = SubmitField()
    
class QuizForm2(FlaskForm):
    question_1 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_2 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_3 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_4 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_5 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    submit = SubmitField()
    
class QuizForm3(FlaskForm):
    question_1 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_2 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_3 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_4 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    question_5 = RadioField(u"Favorite Breakfast Meat", choices=[("bacon", "Bacon"), ("scrapple", "Scrapple"), ("taylor_ham", "Taylor Ham")])
    submit = SubmitField()