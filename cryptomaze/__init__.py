from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from cryptomaze.settings import pri_key, pub_key

app = Flask(__name__)

app.config['SECRET_KEY'] = '0343c517a2005ef9540492aee77c16da'
app.config['RECAPTCHA_PUBLIC_KEY'] = pub_key
app.config['RECAPTCHA_PRIVATE_KEY'] = pri_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptomaze.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'
login_manager.login_message = 'Please enter your Bitcoin Address to access this page.'
login_manager.login_message_category = 'info'

from cryptomaze import routes
