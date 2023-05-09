from mysqlconnection import connectToMySQL

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.food_item=data['food_item']
        self.description=data['description']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELCT * FROM menus;"
        results= connectToMySQL('dojo_n_tacos_db').query_db(query)
        items=[]
        for item in results:
            items.append(cls(item))
        return items

        # No need to put data as a parameter b/c we arent getting anything from forms

    @classmethod
    def create(cls, data):
        query= """
                INSERT INTO menus (food_item, description)
                VALUES (%(food_item)s, %(description)s);
                """
        return connectToMySQL('dojo_n_tacos_db').query_db(query, data)

# if __name__=='__main__':
#     app.run(debug=True)