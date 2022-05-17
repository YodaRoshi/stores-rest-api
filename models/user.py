import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    # auto increment
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    #these two methods are an interface for other part of program to interact with the user things
    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls,_id):
        # Notice _id  instead of id becasue Python has a bulit-in method called id
        return cls.query.filter_by(id=_id).first()
