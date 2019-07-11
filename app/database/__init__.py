# #################################################################################################
# Flask Server Imports
from flask_login import UserMixin
# MongoEngine Imports
import mongoengine as db
# #################################################################################################
# Python Imports
import datetime
# #################################################################################################

db.connect('ChoongPang', alias='default')


class User(UserMixin,db.Document):
    UserUserName = db.StringField()
    UserFirstName = db.StringField()
    UserLastName = db.StringField()
    UserEmail = db.StringField()
    UserPassword = db.StringField()
    UserContactNumber = db.StringField()
    UserAdrress = db.StringField()
    UserType = db.ReferenceField('UserType')
    UserAccess = db.StringField(default = 'Yes')

class UserType(db.Document):
    UserTypeName = db.StringField()

class Business(db.Document):
    BusinessName = db.StringField()
    BusinessDescription = db.StringField()
    BusinessImageUrl = db.StringField()
    BusinessContactNumber = db.StringField()
    BusinessEmail = db.StringField()
    BusinessAddress = db.StringField()

class BusinessHasUsers(db.Document):
    Business = db.ReferenceField(Business)
    User = db.ReferenceField(User)

class BusinessHasProducts(db.Document):
    Business = db.ReferenceField(Business)
    Product = db.ReferenceField('Product')

class Product(db.Document):
    ProductName = db.StringField()
    ProductPrice = db.FloatField()
    ProductCategory = db.ReferenceField('ProductCategory')

class ProductCategory(db.Document):
    ProductCategoryName = db.StringField()

class Advertisement(db.Document):
    AdvertisementTitle = db.StringField()
    AdvertisementDescription = db.StringField()
    AdvertisementImageUrl = db.StringField()
    Business = db.ReferenceField(Business)

class Order(db.Document):
    OrderingCustomer = db.ReferenceField(User)
    DeliveringCustomer = db.ReferenceField(User)
    OrderingTime = db.DateTimeField(default=datetime.datetime.now())
    OrderingTotalAmount = db.FloatField()

class OrderHasProducts(db.Document):
    Order = db.ReferenceField(Order)
    Product = db.ReferenceField(Product)

class Route(db.Document):
    RouteDevisions = db.ListField()
    RouteTrackUrl = db.StringField()
    RouteTime = db.StringField()
    RouteTrackText = db.StringField()

class Payment(db.Document):
    PaymentMethod = db.ReferenceField('PaymentMethods')
    Order = db.ReferenceField(Order)
    PaymentIsPending = db.BooleanField(default=False)
    PaymentUser = db.ReferenceField(User)
    DeliveringUser = db.ReferenceField(User)
    PaymentCommission = db.FloatField()

class PaymentMethods(db.Document):
    PaymentName = db.StringField()

class CommissionPercentageData(db.Document):
    Percentage = db.FloatField(default= 5.0)
