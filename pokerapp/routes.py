from pokerapp import pokerpack, db
from flask import render_template, flash, redirect, url_for, request
from pokerapp.forms import LoginForm, RegistrationForm, QuizForm
from flask_login import current_user, login_user, logout_user, login_required
from pokerapp.models import User, Results
from werkzeug.urls import url_parse
from sqlalchemy.sql import func

#Routes are used to link things. like a hyperlink to another page.

#Splash page route
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
    if form.validate_on_submit(): #checks users login credentials are valid
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

@pokerpack.route('/stats')
def stats():
    #Avg User Results
    avg1 = db.session.query(func.avg(Results.quiz1)).scalar()
    avg2 = db.session.query(func.avg(Results.quiz2)).scalar()
    avg3 = db.session.query(func.avg(Results.quiz3)).scalar()
    avgfinal = db.session.query(func.avg(Results.finalquiz)).scalar()

    #Total number of users completed each quiz
    less1total = db.session.query(func.count(Results.quiz1)).scalar()
    less2total = db.session.query(func.count(Results.quiz2)).scalar()
    less3total = db.session.query(func.count(Results.quiz3)).scalar()
    finaltotal = db.session.query(func.count(Results.finalquiz)).scalar()
    totalusers = db.session.query(func.count(User.username)).scalar()
    return render_template("stats.html", title = "Stats",avg1=avg1, avg2=avg2, avg3=avg3, avgfinal=avgfinal, less1total=less1total, less2total=less2total, less3total=less3total, finaltotal=finaltotal, totalusers=totalusers)

#logout the user on click
@pokerpack.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@pokerpack.route("/register", methods=["GET", "POST"]) #registers user if credentials are valid
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
        return redirect(url_for("login")) #redirects to login page after registration
    return render_template("register.html", title="Register", form=form)

#Lesson routes
#logins are required for lessons
@pokerpack.route("/user/<username>")
@login_required
def user(username): #passes the user information for the charts on the profile page
    user = User.query.filter_by(username=username).first_or_404() 
    userresult = Results.query.filter_by(user_id=current_user.id).first()
    avg1 = db.session.query(func.avg(Results.quiz1)).scalar()
    avg2 = db.session.query(func.avg(Results.quiz2)).scalar()
    avg3 = db.session.query(func.avg(Results.quiz3)).scalar()
    avgfinal = db.session.query(func.avg(Results.finalquiz)).scalar()
    return render_template("user.html", user=user, userresult=userresult, avg1=avg1, avg2=avg2, avg3=avg3, avgfinal=avgfinal)

@pokerpack.route("/lessons") #contains the lesson links, blocked off if not passed previous lessons or not logged in
def lessons():
    quiz1bool = False
    quiz2bool = False
    quiz3bool = False
    if current_user.is_authenticated:
        loggedin = True
        userresult = Results.query.filter_by(user_id=current_user.id).first()
        if userresult is not None:
            if userresult.quiz1 is not None:
                if userresult.quiz1 >= 50:
                    quiz1bool = True
            if userresult.quiz2 is not None:
                if userresult.quiz2 >= 50:
                    quiz2bool = True
            if userresult.quiz3 is not None:
                if userresult.quiz3 >= 50:
                    quiz3bool = True
        return render_template("/Lessons/lessonshome.html", loggedin=loggedin, quiz1bool=quiz1bool, quiz2bool=quiz2bool, quiz3bool=quiz3bool)
    else:
        loggedin = False
        return render_template("/Lessons/lessonshome.html", loggedin=loggedin, quiz1bool=quiz1bool, quiz2bool=quiz2bool, quiz3bool=quiz3bool)

@pokerpack.route("/lesson1", methods=["GET", "POST"]) #directs to lesson 1 with form for database entry
@login_required
def lesson1():
    form = QuizForm()
    if form.validate_on_submit():
        accountcheck = Results.query.filter_by(user_id=current_user.id).first() #if user exists, just update the quiz score
        if accountcheck is not None:
            accountcheck.quiz1=form.score.data
            db.session.commit()
            return redirect(url_for("lessons"))
        else:
            userscore = Results(user_id=current_user.id, quiz1=form.score.data) #if user doesn't exist in results table, makes them a record
            db.session.add(userscore)   
            db.session.commit()
            return redirect(url_for("lessons"))
    return render_template("/Lessons/lesson1.html", form=form)

@pokerpack.route("/lesson2", methods=["GET", "POST"]) #directs to lesson 2 with form for database entry
@login_required
def lesson2():
    form = QuizForm()
    if form.validate_on_submit():
        accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if accountcheck is not None:
            accountcheck.quiz2=form.score.data
            db.session.commit()
            return redirect(url_for("lessons"))
        else:
            userscore = Results(user_id=current_user.id, quiz2=form.score.data)
            db.session.add(userscore)   
            db.session.commit()
            return redirect(url_for("lessons"))
    return render_template("/Lessons/lesson2.html", form=form)

@pokerpack.route("/lesson3", methods=["GET", "POST"]) #directs to lesson 3 with form for database entry
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

@pokerpack.route("/finalquiz", methods=["GET", "POST"]) #directs to final quiz with form for database entry
@login_required
def finalquiz():
    form = QuizForm()
    if form.validate_on_submit():
        accountcheck = Results.query.filter_by(user_id=current_user.id).first()
        if accountcheck is not None:
            accountcheck.finalquiz=form.score.data
            db.session.commit()
            return redirect(url_for('user', username=current_user.username))
        else:
            userscore = Results(user_id=current_user.id, finalquiz=form.score.data)
            db.session.add(userscore)   
            db.session.commit()
            return redirect(url_for('user', username=current_user.username))
    return render_template("/finalquiz.html", form=form)
