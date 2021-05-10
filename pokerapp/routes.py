from pokerapp import pokerpack, db
from flask import render_template, flash, redirect, url_for, request
from pokerapp.forms import LoginForm, RegistrationForm, QuizForm1, QuizForm2, QuizForm3
from flask_login import current_user, login_user, logout_user, login_required
from pokerapp.models import User
from werkzeug.urls import url_parse

@pokerpack.route("/")
@pokerpack.route("/index")
def index():
    return render_template("pokerlanding.html", title="Home")

@pokerpack.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid usernmae of password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)

@pokerpack.route("/assess")
def assess():
    return render_template("assess.html", title = "Assessments")

@pokerpack.route('/stats')
def stats():
    return render_template("stats.html", title = "Stats")

@pokerpack.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@pokerpack.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations! You are now registered!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)

@pokerpack.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {"author": user, "body": "Test post #1"},
        {"author": user, "body": "Test post #2"}
    ]
    return render_template("user.html", user=user, posts=posts)

@pokerpack.route("/lessons", methods=["GET", "POST"])
def lessons():
    if current_user.is_authenticated:
        return render_template("/Lessons/lessonshome.html")
    else:
        return render_template("/Lessons/lessonshomeLOCKED.html")#return render_template("/Lessons/lesson1.html") #change routing

@pokerpack.route("/lesson1")
@login_required
def lesson1():
    quiz_form = QuizForm1()
    return render_template("/Lessons/lesson1.html", quiz_form=quiz_form)

@pokerpack.route("/lesson2")
@login_required
def lesson2():
    quiz_form = QuizForm2()
    return render_template("/Lessons/lesson2.html", quiz_form=quiz_form)

@pokerpack.route("/lesson3")
@login_required
def lesson3():
    quiz_form = QuizForm3()
    return render_template("/Lessons/lesson3.html", quiz_form=quiz_form)
