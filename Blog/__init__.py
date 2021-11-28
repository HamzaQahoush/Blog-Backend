from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'posts.db')
app.config['SECRET_KEY']='25e5d95f9fa4a78c90e9d021'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)





from Blog import routes