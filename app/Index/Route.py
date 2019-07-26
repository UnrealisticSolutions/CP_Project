# ################################################################################################
# Author : Pulasthi Bandara
# Date Started :2019.07.26
# Python Version:3.7
# ################################################################################################

# Flask Server Imports
from flask import *
from flask_login import login_user, current_user, logout_user, login_required
# ################################################################################################


# Python Imports
import datetime
# ################################################################################################

Index = Blueprint('Index', __name__)

@Index.route('/Index',methods = ['GET','POST'])
def Welcome():
    title = 'Welcome'
    date = datetime.datetime.now().year #Getting The Current Time(Footer Signature)
    return render_template('Index/Index.html',date=date)