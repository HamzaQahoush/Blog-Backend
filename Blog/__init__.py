from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os
from configparser import ConfigParser


# import config file to global object
config = ConfigParser()
config_file = '../config.ini'
config.read(config_file)


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'posts.db')
app.config['SECRET_KEY']='25e5d95f9fa4a78c90e9d021'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)
migrate=Migrate(app , db)




from Blog import routes