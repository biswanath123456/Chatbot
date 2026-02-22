# # models.py
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash

# db = SQLAlchemy()

# class User(UserMixin, db.Model):
#     __tablename__ = 'user'
    
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(200), nullable=False)
    
#     def set_password(self, password):
#         """Hash and set password"""
#         self.password_hash = generate_password_hash(password)
    
#     def check_password(self, password):
#         """Check if password matches"""
#         return check_password_hash(self.password_hash, password)
    
#     def __repr__(self):
#         return f'<User {self.username}>'


# models.py
from flask_pymongo import PyMongo
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

mongo = PyMongo()

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.username = user_data['username']
        self.email = user_data['email']
        self.password_hash = user_data['password_hash']
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return User(user_data)
        return None
    
    @staticmethod
    def get_by_username(username):
        """Get user by username"""
        user_data = mongo.db.users.find_one({'username': username})
        if user_data:
            return User(user_data)
        return None
    
    @staticmethod
    def get_by_email(email):
        """Get user by email"""
        user_data = mongo.db.users.find_one({'email': email})
        if user_data:
            return User(user_data)
        return None
    
    @staticmethod
    def create_user(username, email, password):
        """Create a new user"""
        user_data = {
            'username': username,
            'email': email,
            'password_hash': generate_password_hash(password)
        }
        result = mongo.db.users.insert_one(user_data)
        user_data['_id'] = result.inserted_id
        return User(user_data)
    
    def check_password(self, password):
        """Check if password matches"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'