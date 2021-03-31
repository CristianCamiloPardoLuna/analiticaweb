from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

APP = Flask(
    __name__,
    template_folder='./frontend/templates',
    static_folder='./frontend/templates/static'
)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
APP.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
APP.config['SECRET_KEY'] = 'xx' ##
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(APP)