from flask import *


Home = Blueprint('Home', __name__)

@Home.route('/home',methods = ['GET','POST'])
def home():
    return render_template('Home/CustomerHome.html')