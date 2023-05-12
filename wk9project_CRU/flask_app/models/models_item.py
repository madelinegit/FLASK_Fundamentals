# from flask_app.config.mysqlconnection import connectToMySQL #new location i put in manually

from flask_app.config.mysqlconnection import connectToMySQL

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.fooditem=data['fooditem']
        self.description=data['description']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_one(cls, data):
        query= """
                SELECT * FROM menus
                WHERE id = %(id)s
                """
        # results=[]
        results = connectToMySQL('dojo_n_tacos_db').query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query="SELECT * FROM menus;"
        results= connectToMySQL('dojo_n_tacos_db').query_db(query)
        items=[]
        for pineapple in results:
            items.append(cls(pineapple))
        return items

        # No need to put data as a parameter b/c we arent getting anything from forms

    @classmethod
    def create(cls, data):
        query= """
                INSERT INTO menus (fooditem, description)
                VALUES (%(fooditem)s, %(description)s);
                """
        return connectToMySQL('dojo_n_tacos_db').query_db(query, data)

    @classmethod
    def update(cls,form_data, item_id):
        query = f"UPDATE menus SET fooditem = %(fooditem)s, description = %(description)s WHERE id={item_id}"
        return connectToMySQL('dojo_n_tacos_db').query_db(query,form_data)
        #with an F string on an update we cannot do the """"

# if __name__=='__main__':
#     app.run(debug=True)