# ################################################################################################
# Author : Pulasthi Bandara
# Date Started :2019.07.05
# Python Version:3.7
# ################################################################################################

# Flask Server Imports
from flask import *

# Python Imports
import datetime


Home = Blueprint('Home', __name__)

@Home.route('/home',methods = ['GET','POST'])
def home():
    title = 'Home'
    date = datetime.datetime.now().year
    return render_template('Home/CustomerHome.html',date=date)