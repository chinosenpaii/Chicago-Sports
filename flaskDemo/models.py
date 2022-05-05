from datetime import datetime
from flaskDemo import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm

db.Model.metadata.reflect(db.engine)

@login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"


class Matches(db.Model):
    __table__ = db.Model.metadata.tables['Matches']


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

    

  
