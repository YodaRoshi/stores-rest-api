import os

from flask import Flask, render_template # request is for accessing data sent by requests
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList
from security import authenticate, identity # imported from security.py

from db import db

app = Flask(__name__)
# this tells SQLAlchemy database is gonna live at the root folder of the project this can be mySQL or any other databases
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
DATABASE_URL = 'postgresql://pqoikqytwqtpxg:103b0938d6adf8aa0d63a9ceb33770778aadd4b7f932435f7ada88700e4232e3@ec2-3-231-82-226.compute-1.amazonaws.com:5432/d9h19umuit3t1e'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# in order to know when an object had changed but not been saved in the database
# Flask_SQLALCHEMY was tracking every chages that we made to SQLAlchemy sessions
# and that took some resources
# now it's turneed off, because SQLAlchemy itself the  main library has it own modification traker.
# and its better than Flask_SQLALCHEMY

api = Api(app)
app.secret_key = 'jose'
# decolator
db.init_app(app)

# create all the tables if not exist
# SQLAlchemy only crates tables it sees, going through imports.
# that means if if you remove 'from resources.store import Store, StoreList'
# Store and StoreList won't get created

@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)
# this create a new endpoint /auth
# recieve the user info and send it to the authentiate function
@app.route('/') # http://127.0.0.1:5000
def home():
    return render_template('index.html')
# Endpoints
api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    #port 5000 is default thus redundant
