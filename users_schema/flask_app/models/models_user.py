from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db="users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.firstname=data['firstname']
        self.lastname=data['lastname']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_one(cls, data): #no need for data bc no id, it's all of them
        query="""
            SELECT * FROM users WHERE id= %(id)s
            """
        results= connectToMySQL(cls.db).query_db(query, data) #the controller specifies which ID
        return cls(results[0])

    @classmethod
    def get_all(cls): #no need for data bc no id, it's all of them
        query="SELECT * FROM users;"
        # results= connectToMySQL(cls.db).query_db(query)
        results= connectToMySQL(cls.db).query_db(query)
        #return results would look weird like a long dictionary to parse through, so do this:
        users=[]
        for user in results:
            #makes an object
            users.append( cls(user) ) #adds to list userS
        return users

        # No need to put data as a parameter b/c we arent getting anything from forms
#CREATE USER
    @classmethod
    def create(cls, data):
        query= """
                INSERT INTO users (firstname, lastname, email)
                VALUES (%(firstname)s, %(lastname)s, %(email)s);
                """
        #creates new row id
        # result = the rest of what we said up there^ this prevents mysql injection
        return connectToMySQL(cls.db).query_db(query, data)


#UPDATE USER
    @classmethod
    def update(cls, data, user_id):
        query= f"UPDATE users SET firstname=%(firstname)s, lastname=%(lastname)s, email=%(email)s WHERE id={user_id}"
        return connectToMySQL(cls.db).query_db(query,data)