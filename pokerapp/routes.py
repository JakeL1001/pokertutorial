from pokerapp import pokerpack, db
from flask import render_template, flash, redirect, url_for, request
from pokerapp.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from pokerapp.models import User
from werkzeug.urls import url_parse

@pokerpack.route("/")
@pokerpack.route("/index")
@login_required
def index():

    posts = [
        {
            "author": {"username":"John"},
            "body": "nice"
        },
        {
            "author": {"username": "Jhony"},
            "body": "not nice"
        }
    ]
    return render_template("index.html", title="Home", posts=posts)

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