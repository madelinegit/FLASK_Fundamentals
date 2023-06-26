from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
db = 'cardealz2' #global variable
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

class User:
    def __init__(self, data):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #get one for the person's name in jinja
    @classmethod
    def get_one(cls, data):
        query = """
            SELECT * FROM users
            WHERE id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query, data)
        print("GET_ONE_USER RESULTS: ", results)
        return cls(results[0])

    #called in login / user model
    @classmethod
    def get_email(cls, data):
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

    #called in register / user model
    @classmethod
    def create_new_user (cls, newdata):
        query="""
        INSERT INTO users (firstname, lastname, email, password)
        VALUES (%(firstname)s, %(lastname)s, %(email)s, %(password)s);
        """
        return connectToMySQL(db).query_db(query,newdata)

    #called in register / user model
    @staticmethod
    def validate(users):
        isValid = True
        query = "SELECT * FROM users WHERE email=%(email)s"
        results = connectToMySQL(db).query_db(query, users)
        if len(results)>=1:
            isValid=False
            flash("Email is already in use.")
        if len(users['firstname']) < 3:
            isValid=False
            flash("First Name must be at least 2 characters.")
        if len(users['lastname']) < 3:
            isValid=False
            flash("Last Name must be at least 2 characters.")
        if len(users['password']) < 7:
            isValid=False
            flash("Password must be at least 7 characters.")
        if not EMAIL_REGEX.match(users['email']):
            isValid=False
            flash("Please use a real email address.")
        if users['password'] != users['confirm']:
            isValid=False
            flash("Password doesn't match.")
        return isValid

