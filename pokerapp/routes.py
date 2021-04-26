from pokerapp import pokerpack
from flask import render_template, flash, redirect
from pokerapp.forms import LoginForm

@pokerpack.route("/")
@pokerpack.route("/index")
def index():
    user = {"username": "Miguel"}

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
    return render_template("index.html", title="Home", user=user, posts=posts)

@pokerpack.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)