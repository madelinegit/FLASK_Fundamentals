from flask_app.config.mysqlconnection import connectToMySQL


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
    def get_one(cls, data):
        query = """
            SELECT * FROM orders
            WHERE id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        order_data = cls(results[0])
        for orders in results:
            order_data ={
                'id': orders['id'],
                'name': orders['name'],
                'cookie_type': orders['cookie_type'],
                'quantity': orders['quantity'],
                "created_at": orders['orders.created_at'],
                "updated_at": orders['orders.updated_at'],
            }
            #print(orders)
            orders.append(Order(order_data))
            #?
        return order

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL(db).query_db(query)
        order_items = []
        for orders in results:
            order_items.append(cls(orders))
        return order_items

