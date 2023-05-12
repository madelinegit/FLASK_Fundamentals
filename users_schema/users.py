from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.firstname=data['firstname']
        self.lastname=data['lastname']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELECT * FROM users;"
        results= connectToMySQL('users_schema').query_db(query)
        users=[]
        for u in results:
            users.append( cls(u) )
        return users

        # No need to put data as a parameter b/c we arent getting anything from forms

    @classmethod
    def create(cls, data):
        query= """
                INSERT INTO users (firstname, lastname, email)
                VALUES (%(firstname)s, %(lastname)s, %(email)s);
                """
        #creates new row id
        # result = the rest of what we said up there^ this prevents mysql injection
        return connectToMySQL('users_schema').query_db(query, data)