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

# if __name__=='__main__':
#     app.run(debug=True)