# ################################################################################################
# Author : Pulasthi Bandara
# Date Started :2019.07.05
# Python Version:3.7
# ################################################################################################

# Flask Server Imports
from flask import *
from flask_login import login_user, current_user, logout_user, login_required
# ################################################################################################


# Python Imports
import datetime
# ################################################################################################

Home = Blueprint('Home', __name__)

@Home.route('/home',methods = ['GET','POST'])
def home():
    # Check If The User Is Logged In Or Not(Preventing Logged In User Going Back To Login Page)
    if not current_user.is_authenticated:
        return redirect(url_for('LoginRegister.Login'))
    title = 'Home'
    date = datetime.datetime.now().year #Getting The Current Time(Footer Signature)
    if(current_user.UserType.UserTypeName == 'Customer'):
        return render_template('Home/CustomerHome.html',date=date)
    else:
        return render_template('Home/DeliverHome.html',date=date)