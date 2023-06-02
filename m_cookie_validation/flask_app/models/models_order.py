from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


db = 'cookie_validation'

class Order:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_type = data['cookie_type']
        self.quantity = data['quantity']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #if you add to the init after making the DB, this info will not come from DB, it will come from somewhere else, maybe the model file

    @classmethod
    def create_order(cls, data):
        query = """
            INSERT INTO orders (name, cookie_type, quantity)
            VALUES (%(name)s, %(cookie_type)s, %(quantity)s);
            """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT * FROM orders
            WHERE id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        data = cls(results[0])
            #print(orders)
        return data

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL(db).query_db(query)
        order_items = []
        for orders in results:
            order_items.append(cls(orders))
        return order_items

    @classmethod
    def update_order(cls, data, order_id):
        query = f"UPDATE orders SET name= %(name)s,cookie_type=%(cookie_type)s,quantity=%(quantity)s WHERE id = {order_id};"
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def validate_order(order):
        is_valid = True # we assume this is true
        if len(order['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(order['cookie_type']) < 3:
            flash("cookie type must be at least 3 characters.")
            is_valid = False
        if int(order['quantity']) > 50:
            flash("Order size must be 50 or lesser.")
            is_valid = False
        return is_valid


