from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELCT * FROM menus;"
        results= connectToMySQL('users_db').query_db(query)
        users=[]
        for user in results:
            users.append(cls(user))
        return user

        # No need to put data as a parameter b/c we arent getting anything from forms

    @classmethod
    def create(cls, data):
        query= """
                INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name), %(last_name), %(email));
                """
        return connectToMySQL('users_db').query_db(query, data)