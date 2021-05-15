from pokerapp import pokerpack, db
from flask import render_template, flash, redirect, url_for, request
from pokerapp.forms import LoginForm, RegistrationForm, QuizForm
from flask_login import current_user, login_user, logout_user, login_required
from pokerapp.models import User, Results
from werkzeug.urls import url_parse
from sqlalchemy.sql import func

#Routes are used to link things. like a hyperlink to another page.

#splash page route
@pokerpack.route("/")
@pokerpack.route("/Home")
def home():
    return render_template("pokerlanding.html", title="Home")

#Major login route
@pokerpack.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('No account exists with that username, Please Register')
            return redirect(url_for('register'))
        if not user.check_password(form.password.data):
            flash("Incorrect Password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)

#extra page routes
@pokerpack.route("/assess")
def assess():
    return render_template("assess.html", title = "Assessments")

@pokerpack.route('/stats')
def stats():
    #Avg User Results
    avg1 = db.session.query(func.avg(Results.quiz1)).scalar()
    avg2 = db.session.query(func.avg(Results.quiz2)).scalar()
    avg3 = db.session.query(func.avg(Results.quiz3)).scalar()
    avgfinal = db.session.query(func.avg(Results.total)).scalar()

    less1total = db.session.query(func.count(Results.quiz1)).scalar()
    less2total = db.session.query(func.count(Results.quiz2)).scalar()
    less3total = db.session.query(func.count(Results.quiz3)).scalar()
    finaltotal = db.session.query(func.count(Results.total)).scalar()
    totalusers = db.session.query(func.count(User.username)).scalar()
    return render_template("stats.html", title = "Stats",avg1=avg1, avg2=avg2, avg3=avg3, avgfinal=avgfinal, less1total=less1total, less2total=less2total, less3total=less3total, finaltotal=finaltotal, totalusers=totalusers)

#login routes pt2
@pokerpack.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@pokerpack.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
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
    userResult = Results.query.filter_by(user_id=current_user.id).first()
    avg1 = db.session.query(func.avg(Results.quiz1)).scalar()
    avg2 = db.session.query(func.avg(Results.quiz2)).scalar()
    avg3 = db.session.query(func.avg(Results.quiz3)).scalar()
    avgfinal = db.session.query(func.avg(Results.total)).scalar()
    return render_template("user.html", user=user, userResult=userResult, avg1=avg1, avg2=avg2, avg3=avg3, avgfinal=avgfinal)

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
        accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if accountcheck is not None:
            accountcheck.quiz1=form.score.data
            db.session.commit()
            return redirect(url_for("lesson2"))
        else:
            userscore = Results(user_id=current_user.id, quiz1=form.score.data)
            db.session.add(userscore)   
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
        accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if accountcheck is not None:
            accountcheck.quiz2=form.score.data
            db.session.commit()
            return redirect(url_for("lesson3"))
        else:
            userscore = Results(user_id=current_user.id, quiz2=form.score.data)
            db.session.add(userscore)   
            db.session.commit()
            return redirect(url_for("lesson3"))
    return render_template("/Lessons/lesson2.html", form=form)

@pokerpack.route("/lesson3", methods=["GET", "POST"])
@login_required
def lesson3():
    form = QuizForm()
    if form.validate_on_submit():
        accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if accountcheck is not None:
            accountcheck.quiz3=form.score.data
            db.session.commit()
            return redirect(url_for("lessons"))
        else:
            userscore = Results(user_id=current_user.id, quiz3=form.score.data)
            db.session.add(userscore)   
            db.session.commit()
            return redirect(url_for("lessons"))
    return render_template("/Lessons/lesson3.html", form=form)

@pokerpack.route("/finalquiz", methods=["GET", "POST"])
@login_required
def finalquiz():
    form = QuizForm()
    if form.validate_on_submit():
        accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if accountcheck is not None:
            accountcheck.total=form.score.data
            db.session.commit()
            return redirect(url_for('user', username=current_user.username))
        else:
            userscore = Results(user_id=current_user.id, total=form.score.data)
            db.session.add(userscore)   
            db.session.commit()
            return redirect(url_for('user', username=current_user.username))
    return render_template("/finalquiz.html", form=form)



@pokerpack.route("/submit", methods=["GET", "POST"])
@login_required
def submit():
    
    #if form.validate_on_submit():
        
    return render_template("/Lessons/lessonshome.html")
