# ################################################################################################
# Author : Pulasthi Bandara
# Date Started :2019.06.25
# Python Version:3.7
# ################################################################################################

# Flask Server Imports
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# ################################################################################################

# App Imports
from app.config import Config
from app.database import User
# ################################################################################################

# Python Imports
from logging import FileHandler, WARNING #(For Log File Creating)
# ################################################################################################

# Creating Flask Object
app = Flask(__name__)
# BCrypt Object For Encrypting Data
bcrypt = Bcrypt(app)

# Login Manager Object
login_manager = LoginManager(app)
login_manager.login_view = 'User.login'
login_manager.login_message_category  = 'info'

# User Loader For Login Operation
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

#Log File To Detect Errors
file_handler = FileHandler('ErrorLog.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

# Login Routes
from app.RegisterLogin.Route import LoginRegister
# User HomePage(Dashboard) Routes
from app.Home.Route import Home
#Index Page Routes
from app.Index.Route import Index

app.config.from_object(Config)

app.register_blueprint(LoginRegister)
app.register_blueprint(Home)
app.register_blueprint(Index)
