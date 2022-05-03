from datetime import datetime
from flaskDemo import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm

db.Model.metadata.reflect(db.engine)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.userID}', '{self.image_file}')"


class Post(db.Model):
     __table_args__ = {'extend_existing': True}
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(100), nullable=False)
     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     content = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

     def __repr__(self):
         return f"Post('{self.title}', '{self.date_posted}')"



class Matches(db.Model):
    __table__ = db.Model.metadata.tables['Matches']

'''    
class Team(db.Model):
    __table__ = db.Model.metadata.tables['Team']
'''
# used for query_factory
def getMatches(columns=None):
    u = Matches.query
    if columns:
        u = u.options(orm.load_only(*columns))
    return u


def getMatchesFactory(columns=None):
    return partial(getMatches, columns=columns)

class Team(db.Model):
    __table__ = db.Model.metadata.tables['Team']

class Opponent(db.Model):
    __table__ = db.Model.metadata.tables['Opponent']
    
class Sport(db.Model):
    __table__ = db.Model.metadata.tables['Sport']
'''
class Project(db.Model):
    __table__ = db.Model.metadata.tables['opponent']
class Matches(db.Model):
    __table__ = db.Model.metadata.tables['']
'''
    

  
