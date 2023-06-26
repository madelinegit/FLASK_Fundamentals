from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models.models_user import User
db = 'cardealz2' #(global variable)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.price = data['price']
        self.model = data['model']
        self.make = data['make']
        self.year = data['year']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def get_one_car(cls, data):
        query = """
        SELECT * FROM cars
        WHERE id = %(id)s;
        """
        results=connectToMySQL(db).query_db(query, data)
        print("GET ONE CAR RESULTS: ", results)
        return cls(results[0])

    @classmethod
    def get_one_car_with_user(cls, seller_data):
        query = """
            SELECT * FROM cars
            JOIN users
            ON cars.user_id = users.id
            WHERE cars.id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query)
        print("GET ONE CAR / USER RESULTS: ", results)
        sellers=[]
        for user in results:
            one_seller = cls(user)
            seller_data = {
                    'id' : user['users.id'],
                    'firstname' : user['firstname'],
                    'lastname' : user['lastname'],
                    'email' : user['email'],
                    'password' : user['password'],
                    'created_at' : user['created_at'],
                    'updated_at' : user['updated_at']
            }
            one_seller= User(seller_data)
            sellers.append(one_seller)
            print("ONE_SELLER: ", one_seller)
            print("SELLERS: ", sellers)
        return cls(results[0])

#ISSUE: something with the DB, Results always come back as FALSE for my get one join.
# I tried a separate query below, commented out, a slighly different way than I normally
# would write (sourced online), in order to troubleshoot. The same thing happened so I
# thought this must be due to my decision to use a float instead of a decimal for the price.
# I continued to create the second database, i used INT because well, I'm more used to that one
#and wanted to make it work even if it doesn't allow me to use decimals.
# So anyways, after the code below rendered the same error, I then re-created the DB, suspecting
# that my use of data types other than VARCHAR had thrown things off.

    # @classmethod
    # def get_one_car_with_user(cls, seller_data):
    #     query = """
    #         SELECT cars.*, users.id AS user_id, users.firstname, users.lastname, users.email, users.password, users.created_at, users.updated_at
    #         FROM cars
    #         JOIN users ON cars.user_id = users.id
    #         WHERE cars.id = %(car_id)s;
    #         """
    #     results = connectToMySQL(db).query_db(query)
    #     print("GET ONE CAR / USER RESULTS: ", results)
    #     sellers=[]
    #     RESULTS CAME BACK FALSE
    #     return cls(results[0])

    #get all cars with user: called in dashboard car controller
    @classmethod
    def get_all_cars_with_user(cls):
        query = """
            SELECT * FROM cars
            JOIN users
            ON cars.user_id = users.id;
            """
        results = connectToMySQL(db).query_db(query)
        print("GET ALL CARS /USER RESULTS: ", results)
        sellers=[]
        for user in results:
            one_seller = cls(user)
            seller_data = {
                    'id' : user['users.id'],
                    'firstname' : user['firstname'],
                    'lastname' : user['lastname'],
                    'email' : user['email'],
                    'password' : user['password'],
                    'created_at' : user['created_at'],
                    'updated_at' : user['updated_at']
            }
            one_seller= User(seller_data)
            sellers.append(one_seller)
            print("ONE_SELLER: ", one_seller)
            print("SELLERS: ", sellers)
        return results


    @classmethod
    def car_create (cls, newdata):
        query="""
        INSERT INTO cars (price, model, make, year, description, user_id)
        VALUES (%(price)s, %(model)s, %(make)s, %(year)s, %(description)s, %(user_id)s);
        """
        print("RAN CAR QUERY")
        return connectToMySQL(db).query_db(query, newdata)

    @classmethod
    def update (cls, form_data, id):
        query = f"UPDATE cars SET price = %(price)s, model = %(model)s, make = %(make)s, year = %(year)s, description = %(description)s WHERE id={id};"
        #don't mention foreign key
        return connectToMySQL(db).query_db(query, form_data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    #Static Method
    @staticmethod
    def car_validate(car):
        print ("CAR: ", car)
        isValid = True
        required_feilds=['price', 'model', 'make', 'year', 'description']
        for field in required_feilds:
            if field not in car:
                isValid = False
                print("INVALID ENTRY")
                flash("All Feilds Required.")
        #if INT and FLOAT <= 0,
        # isValid=False
        # flash("Price//Year must be greater than zero.")
        if len(car['price']) <4:
            isValid=False
            flash("Please enter the price (only numbers not characters or commas.)")
        if len(car['model']) <3:
            isValid=False
            flash("Model name must be longer.")
        if len(car['make']) <3:
            isValid=False
            flash("Make name must be longer.")
        if len(car['year']) <4:
            isValid=False
            flash("Enter a four digit numeric year.")
        if len(car['description']) < 3:
            isValid=False
        return isValid
