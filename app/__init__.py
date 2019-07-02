from flask import Flask
from flask_bcrypt import Bcrypt
from app.config import Config
from app.database import User
from logging import FileHandler, WARNING

app = Flask(__name__)
bcrypt = Bcrypt(app)

#Log File To Detect Errors
file_handler = FileHandler('ErrorLog.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

from app.RegisterLogin.Route import LoginRegister

app.config.from_object(Config)

app.register_blueprint(LoginRegister)
