import os
class Config():

	os.environ['EMAIL_USER'] = ''
	os.environ['EMAIL_PASS'] = ''
	SECRET_KEY = '0e4480cd48ea25e8e0b79cf20d1759a2'
	MONGO_URI = "mongodb://localhost:27017/ChoongPang"
	MAIL_SERVER = 'smtp.googlemail.com'
	SERVER_NAME = '127.0.0.1:5000'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
	TESTING = False
	UPLOAD_FOLDER = '/home/scorpio/Documents/Cloned/CP_Project/app/static/Images/BusinessProfile/'
	ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
	DEFAULT_BUSINESS_IMAGE_NAME = 'DefaultBusiness.png'
	DEFAULT_BUSINESS_IMAGE_PATH = '/home/scorpio/Documents/Cloned/CP_Project/app/static/Images/BusinessProfile/'
	# app.instance_path