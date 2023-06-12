from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# from flask_app.models.models_users import User
db = 'login_registration_wk13' #global variable
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')# object
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

class User:
    #db = 'login_registration_wk13'
    #class variable is any variable i declare here
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def save (cls, data):
        query="""
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT * FROM users
            WHERE id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        if len(results) <1:
            print("came back false")
            return False
        print("one result")
        return cls(results[0])
            #print(orders)

    @classmethod
    def getEmail(cls, data):
        query= """
            SELECT * FROM users
            WHERE email = %(email)s;
            """
        results= connectToMySQL(db).query_db(query, data)
        print("results from model:", results)
        if len(results) < 1:
            print ("came back false")
            return False
        print("one result")
        return cls(results[0])

    @staticmethod
    def validate(users):
        isValid = True
        query = "SELECT * FROM users WHERE email=%(email)s"
        results = connectToMySQL(db).query_db(query, users)
        if len(results)>=1:
            isValid=False
            flash("Email is already in use.")
        if len(users['first_name']) < 3:
            isValid=False
            flash("Name must be at least 3 characters.")
        if len(users['last_name']) < 3:
            isValid=False
            flash("Name must be at least 3 characters.")
        if len(users['password']) < 7:
            isValid=False
            flash("Password must be at least 7 characters.")
        if not EMAIL_REGEX.match(users['email']):
            isValid=False
            flash("please use a real email address.")
        if not PASSWORD_REGEX.match(users['password']):
            isValid=False
            flash("please use at least one number, & uppercase + lowercase letters.")
        if users['password'] != users['confirm']:
            isValid=False
            flash("Password doesn't match.")
        return isValid

        #     isValid = False
        # if len(order['cookie_type']) < 3:
        #     flash("cookie type must be at least 3 characters.")
        #     is_valid = False
        # if int(order['quantity']) > 50:
        #     flash("Order size must be 50 or lesser.")
        #     is_valid = False
        # return is_valid