from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError,Regexp
from wtforms_sqlalchemy.fields import QuerySelectField
from flaskDemo import db
from flaskDemo.models import User, Matches, getMatches, getMatchesFactory, Team, Opponent, Sport
from wtforms.fields import DateField

match = Matches.query.with_entities(Matches.teamName, Matches.arena, Matches.sport).distinct()

myChoices4 = [(row[0],row[0]) for row in match] 
results=list()
for row in (match):
    rowDict=row._asdict()
    results.append(rowDict)
myChoices = [(row['teamName'],row['teamName']) for row in results]
myChoices2 = [(row['arena'], row['arena']) for row in results]
myChoices3 = [(row['sport'], row['sport']) for row in results]
regex1='^((((19|20)(([02468][048])|([13579][26]))-02-29))|((20[0-9][0-9])|(19[0-9][0-9]))-((((0[1-9])'
regex2='|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))$'
regex=regex1 + regex2


class AssignForm(FlaskForm):
    Employee = SelectField('Employee')
    Project = SelectField('Project')
    submit = SubmitField('Assign')


    def selectFieldChoices(self):
        results = db.session.query(Employee).order_by(Employee.lname.asc()).all()
        employees = list()
        for result in results:
            employees.append((str(result.ssn), str(result.lname)))
        results = db.session.query(Project).order_by(Project.pname.asc()).all()
        projects = list()
        for result in results:
            projects.append((str(result.pnumber), str(result.pname)))
        self.Employee.choices = employees
        self.Project.choices = projects


class RemoveForm(FlaskForm):
    Employee = SelectField('Employee')
    Project = SelectField('Project')
    submit = SubmitField('Delete')

    def selectFieldChoices(self):
        results = db.session.query(Employee).order_by(Employee.lname.asc()).all()
        employees = list()
        for result in results:
            employees.append((str(result.ssn), str(result.lname)))
        results = db.session.query(Project).order_by(Project.pname.asc()).all()
        projects = list()
        for result in results:
            projects.append((str(result.pnumber), str(result.pname)))
        self.Employee.choices = employees
        self.Project.choices = projects


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('UserID',
                           validators=[DataRequired(), Length(min=2, max=20)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That UserID is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

    
class MatchUpdateForm(FlaskForm):

    matchID = HiddenField("")

    matchID=StringField('Match ID:', validators=[DataRequired(),Length(max=15)])

    score = StringField("Match Score", validators=[DataRequired()])  # myChoices defined at top
    arena = SelectField("Arena", choices=myChoices2)
    matchType = StringField("Match Type", validators=[DataRequired()])
    status = StringField("Status", validators=[DataRequired()])
    teamName = SelectField("Team Name", choices=myChoices)
    oppName = StringField("Opponents Name", validators=[DataRequired()])
    sport = SelectField("Sport", choices=myChoices3)
    date = DateField("Match Date:", format='%Y-%m-%d')  # This is using the html5 date picker (imported)
    submit = SubmitField('Update this match')

    def validate_dname(self, matchID): 
         if match and (str(match.matchID) != str(self.matchID.data)):
             raise ValidationError('That match ID is already being used. Please choose a different ID.')


class MatchForm(MatchUpdateForm):

    matchID=IntegerField('Match ID', validators=[DataRequired()])
    submit = SubmitField('Add this match')

    def validate_matchID(self, matchID):   
        match = Matches.query.filter_by(matchID=matchID.data).first()
        if match:
            raise ValidationError('That match ID is taken. Please choose a different one.')

