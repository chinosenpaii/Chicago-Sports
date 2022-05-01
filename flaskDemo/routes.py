import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskDemo import app, db, bcrypt
from flaskDemo.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, MatchForm,MatchUpdateForm, AssignForm
from flaskDemo.models import User, Post, Matches, Team, Opponent, Sport
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

#Looking at the database, I think we query through just matchID since it is the only primary key unlike the last lab -
# - where it had two primary keys (essn, pno), which led to the results2 join
@app.route("/")
@app.route("/home")
def home():
    results= Matches.query.with_entities(Matches.matchID).all()
    return render_template('assign_home.html', joined_m_n = results)
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

#Picture for profile, see if we can convert to adding picture to Chicago teams on posts
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

@app.route("/assign/<matchID>/new", methods=['GET', 'POST'])
def new_match(matchID):
    form = DeptForm()
    if form.validate_on_submit():
        match = Matches(score=form.score.data, arena=form.arena.data, matchType=form.matchType.data, status=form.status.data, date=form.date.data, teamName=form.teamName.data, oppName=form.oppName.data, sport=form.sport.data)
        db.session.add(assign)
        db.session.commit()
        flash('You have added a new match!', 'success')
        return redirect(url_for('home'))
    return render_template('create_dept.html', title='New Match',
                           form=form, legend='New Match')
'''
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
'''

@app.route("/matches/<matchID>")
def match(matchID):
    assign = Matches.query.get_or_404([matchID])
    #return render_template('assign.html', title=str(match.teamName)+"_"+ str(match.oppName)+"_"+ str(match.sport), match=match, now=datetime.utcnow())
    return render_template('assign.html', title=match.matchID, match=match, now=datetime.utcnow())

#Update
@app.route("/match/<matchID>/update", methods=['GET', 'POST'])
@login_required
def update_match(matchID):
    #return "update page under construction"
    match = Matches.query.get_or_404(matchID)
    currentMatch = match.matchID
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
        match.score=form.score.data
        match.arena=form.arena.data
        match.matchType=form.matchType.data
        match.status=form.status.data 
        match.date=form.date.data
        match.teamName=form.teamName.data
        match.oppName=form.oppName.data
        match.sport=form.sport.data
    return render_template('create_dept.html', title='Update Match',
                           form=form, legend='Update Match')



#Delete
@app.route("/matches/<matchID>/delete", methods=['POST'])
@login_required
def delete_match(matchID):
    match = Matches.query.get_or_404([matchID])
    db.session.delete(match)
    db.session.commit()
    flash('The match has been deleted!', 'success')
    return redirect(url_for('home'))
