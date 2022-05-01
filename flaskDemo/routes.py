import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskDemo import app, db, bcrypt
from flaskDemo.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, MatchForm,MatchUpdateForm, AssignForm
from flaskDemo.models import User, Post, Matches, Team, Opponent, Sport
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


@app.route("/")
@app.route("/home")
def home():
    #results= Works_On.query.with_entities(Works_On.essn).all()
    #return render_template('assign_home.html', joined_m_n = results)
    results2 = Matches.query.join(Team,Matches.teamName == Team.teamName) \
               .add_columns(Team.teamName) \
               .join(Opponent, Opponent.oppName == Matches.oppName).add_columns(Opponent.oppName)
    return render_template('assign_home.html', title='Join',joined_m_n=results2)

   


@app.route("/about")
def about():
    return render_template('about.html', title='About')

#Might not need but might to fill in user data as a requirement
'''
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
'''

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/assign/<pno>/<essn>/new", methods=['GET', 'POST'])
def new_assign(pno, essn):
    form = DeptForm()
    if form.validate_on_submit():
        assign = Works_On(essn=form.ssn.data, pno=form.pnumber.data,hours=0)
        db.session.add(assign)
        db.session.commit()
        flash('You have added a new assignment!', 'success')
        return redirect(url_for('home'))
    return render_template('create_dept.html', title='New Assignment',
                           form=form, legend='New Assignment')

@app.route("/assign/<pno>/<essn>/new", methods=['GET', 'POST'])
def assign():
    form = AssignForm()
    form.selectFieldChoices() 
    if form.validate_on_submit():
        pno = form.Project.data
        essn = form.Employee.data
        assignCheck = Works_On.query.filter_by(essn = essn).filter_by(pno = pno).all()
        if assignCheck:
            flash('Assignment already exists', 'error')
            return render_template('assign_home.html', title = 'Assign', form = form)
        assign = Works_On(essn = essn, pno = pno, hours=0)
        db.session.add(assign)
        db.session.commit()
        flash('Assignment Successful', 'success')
        return redirect(url_for('home'))
    return render_template('assign_home.html', title='Assign Employee to Project', form=form)


@app.route("/matches/<teamName>/<oppName>")
def match(teamName, oppName, sport):
    assign = Matches.query.get_or_404([teamName, oppName, sport])
    return render_template('assign.html', title=str(match.teamName)+"_"+ str(match.oppName)+"_"+ str(match.sport), match=match, now=datetime.utcnow())


@app.route("/match/<teamName>/<oppName>/<sport>/update", methods=['GET', 'POST'])
@login_required
def update_match(teamName, oppName, sport):
    #return "update page under construction"
    match = Matches.query.get_or_404(teamName, oppName, sport)
    currentMatch = assign.matchID
#matchID or teamName
    form = MatchUpdateForm()
    if form.validate_on_submit():          # notice we are are not passing the dnumber from the form
        if currentMatch !=form.matchID.data:
            match.score=form.score.data
        match.arena=form.arena.data
        match.matchType=form.matchType.data
        match.status=form.status.data 
        match.date=form.date.data
        match.teamName=form.teamName.data
        match.oppName=form.oppName.data
        match.sport=form.sport.data
        db.session.commit()
        flash('Your Match has been updated!', 'success')
        return redirect(url_for('match', matchID=matchID))
    elif request.method == 'GET':              # notice we are not passing the dnumber to the form

        match.matchID=form.matchID.data
        match.score=form.score.data
        match.arena=form.arena.data
        match.matchType=form.matchType.data
        match.status=form.status.data 
        match.date=form.date.data
        match.teamName=form.teamName.data
        match.oppName=form.oppName.data
        match.sport=form.sport.data
    return render_template('create_dept.html', title='Update Department',
                           form=form, legend='Update Department')




@app.route("/matches/<teamName>/<oppName>/<sport>delete", methods=['POST'])
@login_required
def delete_match(teamName, oppName, sport):
    assign = Matches.query.get_or_404([teamName, oppName, sport])
    db.session.delete(assign)
    db.session.commit()
    flash('The match has been deleted!', 'success')
    return redirect(url_for('home'))
