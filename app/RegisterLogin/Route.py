# ################################################################################################
# Author : Pulasthi Bandara
# Date Started :2019.06.25
# Python Version:3.7
# ################################################################################################

# Flask Server Imports
from flask import *
from flask_login import login_user, current_user, logout_user, login_required
# ################################################################################################

# Python Imports
import datetime
# ################################################################################################

# App Imports
from app.database import User, UserType, Business, BusinessHasUsers
from app import bcrypt
# ################################################################################################


LoginRegister = Blueprint('LoginRegister', __name__)


@LoginRegister.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        username = request.form['UserName']
        password = request.form['Password']
        remember = False
        if(request.form['Remember'] == 'Yes'):
            remember = True
        # Taking The User Object From The DB
        checkUserNameDB = User.objects(UserUserName = username).first()
        # Checking If The User Object Found Or Not
        if(checkUserNameDB):
            # Compairing The Passwords
            if(bcrypt.check_password_hash(str(checkUserNameDB.UserPassword),password)):
                # Checking If The User Has Access Or Not
                if(checkUserNameDB.UserAccess == 'Yes'):
                    login_user(checkUserNameDB, remember = remember)
                    message = 'Successfully Loged In!'
                    JsonResponse = {'Type': 'Success', 'Message': message}
                    return jsonify(JsonResponse)
                else:
                    message = 'User Blocked! ,Please Contact The Developers!'
                    JsonResponse = {'Type': 'Warning', 'Message': message}
                    return jsonify(JsonResponse)
            else:
                message = 'Invalid Password!'
                JsonResponse = {'Type': 'Warning', 'Message': message}
                return jsonify(JsonResponse)
        else:
            message = 'User Not Found! ,Check Your Username!'
            JsonResponse = {'Type': 'Warning', 'Message': message}
            return jsonify(JsonResponse)
    title = 'User Login'
    date = datetime.datetime.now().year
    # Checking If The User Types Are In The Database Or Not. If Not Default User Types Will Be Added Automatically In This Route
    CheckUserTypes = UserType.objects()
    if not CheckUserTypes:
        UserType(UserTypeName='Customer').save()
        UserType(UserTypeName='Bussinessmen').save()
    # Login Section Header Title
    headerTitle = 'Login'
    return render_template('Login/Login.html', title=title, date=date,headerTitle=headerTitle)


@LoginRegister.route('/Register', methods=['GET', 'POST'])
def Register():
    title = 'Register User'
    date = datetime.datetime.now().year
    # User Register Section(ajax POST Request)
    if request.method == 'POST':
        # Gathering Data From POST Request
        UserNameInput = request.form['UserName']
        FirstNameInput = request.form['FirstName']
        LastNameInput = request.form['LastName']
        EmailAddressInput = request.form['EmailAddress']
        AddressInput = request.form['Address']
        ContactNumberInput = request.form['ContactNumber']
        UserTypeNameInput = request.form['UserType']
        PasswordInput = request.form['Password']
        # Hashing The Password For Protection
        HashedPassword = bcrypt.generate_password_hash(PasswordInput)

        # Gathering UserType Object From The Selected Value
        UserTypeObject = UserType.objects(
            UserTypeName=UserTypeNameInput).first()

        # If UserType Object Not Found Returning a Error Message To The Ajax Request
        if(not UserTypeObject):
            Error_Message = 'Server Error!, Please Contact The Maintainance'
            JsonResponse = {'Type': 'Error', 'Message': Error_Message}
            return jsonify(JsonResponse)
        # Creating A New User Object And Saving
        CheckMail = User.objects(UserEmail=EmailAddressInput).first()
        CheckUserName = User.objects(UserUserName=UserNameInput).first()
        if CheckMail:
            Message = 'Email Already Taken!'
            JsonResponse = {'Type': 'Warning', 'Message': Message}
            return jsonify(JsonResponse)
        if CheckUserName:
            Message = 'Username Already Taken!'
            JsonResponse = {'Type': 'Warning', 'Message': Message}
            return jsonify(JsonResponse)
        Return_User = User(UserUserName=UserNameInput, UserFirstName=FirstNameInput, UserLastName=LastNameInput, UserEmail=EmailAddressInput, UserPassword=HashedPassword, UserContactNumber=ContactNumberInput, UserAdrress=AddressInput, UserType=UserTypeObject).save()
        Message = 'Your Account Has Been Successfully Created!'
        # Returning the Url Of The Next Rendering Page according To The User Type
        if UserTypeNameInput == 'Businessmen':
            JsonResponse = {'Type': 'Success','Message': Message, 'NextURL': 'addBusinessDetails?UserId='+str(Return_User.id)}
        else:
            JsonResponse = {'Type': 'Success','Message': Message, 'NextURL': 'Register'}
        return jsonify(JsonResponse)
    return render_template('Register/Register.html', title=title, date=date)


@LoginRegister.route('/addBusinessDetails', methods=['GET', 'POST'])
def addBussinessDetails():
    title = 'Add Business Details!'
    date = datetime.datetime.now().year
    if request.method == 'POST':
        BusinessName = request.form['BusinessName']
        
    # Get User Id From A Get Request And Get The User Object
    UserObj = User.objects.get(id=request.args.get('UserId'))
    return render_template('Register/AddBusinessDetails/AddBusinessDetails.html',User = UserObj)

# Route to send UserTypes To The Page To Show Select Fields
@LoginRegister.route('/getUserTypes', methods=['GET'])
def getUserTypes():
    ResultVal = UserType.objects()
    return ResultVal.to_json()
