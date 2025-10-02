from flask import Flask
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    username = db.Column(db.String(150), default="Anonymous")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('post.id'))  # For replies
    
    author = db.relationship('User', backref=db.backref('posts', lazy=True))
    replies = db.relationship('Post', 
                            backref=db.backref('parent', remote_side=[id]), 
                            lazy=True,
                            order_by='Post.date.asc()')  # Order replies by date