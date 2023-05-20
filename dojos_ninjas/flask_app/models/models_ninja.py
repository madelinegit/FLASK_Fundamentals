from flask_app.config.mysqlconnection import connectToMySQL

db = 'dojos_ninjas'

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM ninjas
                WHERE id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(db).query_db(query)
        ninja_items = []
        for ninjas in results:
            ninja_items.append(cls(ninjas))
        return ninja_items

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO ninjas ( dojo_id, first_name, last_name, age )
                VALUES ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s );
                """ #lower - values have to match html or what a renamed this to in the controller , not necessarily here
        return connectToMySQL(db).query_db(query, data)

