from pokerapp import pokerpack, db
from flask import render_template, flash, redirect, url_for, request
from pokerapp.forms import LoginForm, RegistrationForm, QuizForm
from flask_login import current_user, login_user, logout_user, login_required
from pokerapp.models import User, Results
from werkzeug.urls import url_parse

#Routes are used to link things. like a hyperlink to another page.

#splash page route
@pokerpack.route("/")
@pokerpack.route("/index")
def index():
    return render_template("pokerlanding.html", title="Home")

#Major login route
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

#extra page routes
@pokerpack.route("/assess")
def assess():
    return render_template("assess.html", title = "Assessments")

@pokerpack.route('/stats')
def stats():
    return render_template("stats.html", title = "Stats")


#login routes pt2
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

#Lesson routes
#logins are required for lessons
@pokerpack.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {"author": user, "body": "Test post #1"}
    ]
    return render_template("user.html", user=user, posts=posts)

@pokerpack.route("/lessons")
def lessons():
    if current_user.is_authenticated:
        return render_template("/Lessons/lessonshome.html")
    else:
        return render_template("/Lessons/lessonshomeLOCKED.html")#return render_template("/Lessons/lesson1.html") #change routing

@pokerpack.route("/lesson1", methods=["GET", "POST"])
@login_required
def lesson1():
    #return render_template("/Lessons/lessonshomeLOCKED.html")
    form = QuizForm()
    if form.validate_on_submit():
        Accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if Accountcheck is not None:
            Accountcheck.quiz1=form.score.data
            db.session.commit()
            return redirect(url_for("lesson2"))
        else:
            UserScore = Results(user_id=current_user.id, quiz1=form.score.data)
            db.session.add(UserScore)   
            db.session.commit()
            return redirect(url_for("lesson2"))
    #else:
        #return render_template("/Lessons/lessonshomeLOCKED.html")
    return render_template("/Lessons/lesson1.html", form=form)

@pokerpack.route("/lesson2", methods=["GET", "POST"])
@login_required
def lesson2():
    form = QuizForm()
    if form.validate_on_submit():
        Accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if Accountcheck is not None:
            Accountcheck.quiz2=form.score.data
            db.session.commit()
            return redirect(url_for("lesson3"))
        else:
            UserScore = Results(user_id=current_user.id, quiz2=form.score.data)
            db.session.add(UserScore)   
            db.session.commit()
            return redirect(url_for("lesson3"))
    return render_template("/Lessons/lesson2.html", form=form)

@pokerpack.route("/lesson3", methods=["GET", "POST"])
@login_required
def lesson3():
    form = QuizForm()
    if form.validate_on_submit():
        Accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if Accountcheck is not None:
            Accountcheck.quiz3=form.score.data
            db.session.commit()
            return redirect(url_for("lessons"))
        else:
            UserScore = Results(user_id=current_user.id, quiz3=form.score.data)
            db.session.add(UserScore)   
            db.session.commit()
            return redirect(url_for("lessons"))
    return render_template("/Lessons/lesson3.html", form=form)

@pokerpack.route("/submit", methods=["GET", "POST"])
@login_required
def submit():
    
    #if form.validate_on_submit():
        
    return render_template("/Lessons/lessonshome.html")
