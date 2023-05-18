from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojo_n_tacos_db'

class Item:

    def __init__(self, data):
        self.id = data['id']
        self.food_item = data['food_item']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM menus
                WHERE id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM menus;"
        results = connectToMySQL(db).query_db(query)
        items = []
        for pineapple in results:
            items.append(cls(pineapple))
        return items

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO menus ( food_item, description, price )
                VALUES ( %(food_item)s, %(description)s, %(price)s );
                """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update(cls, form_data, item_id):
        query = f"UPDATE menus SET food_item = %(food_item)s, description = %(description)s, price = %(price)s WHERE id = {item_id};"
        return connectToMySQL(db).query_db(query, form_data)
    

    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM menus
                WHERE id = %(id)s
                """
        return connectToMySQL(db).query_db(query, data)