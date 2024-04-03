from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    data = db.Column(db.String(1000000))
    title = db.Column(db.String(10000))
    privacy = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    userid = db.Column(db.String(100),db.ForeignKey('user.id'))

class Workspace(db.Model):
    workid = db.Column(db.String(100), primary_key=True)
    name=db.Column(db.String(150),nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(500))
    name = db.Column(db.String(150))
    workid=db.Column(db.String(100),db.ForeignKey('workspace.workid'))
    notes=db.relationship('Note')
    workspace=db.relationship('Workspace')

