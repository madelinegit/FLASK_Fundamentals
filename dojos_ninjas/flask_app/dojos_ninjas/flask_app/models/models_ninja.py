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
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM ninjas
                WHERE id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls, data):
        query = """
            SELECT * FROM ninjas
            JOIN dojos
            ON dojos.id = ninjas.dojo_id
            WHERE dojo.id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query)
        ninja_items = []
        for ninja in results:
            one_ninja = cls(ninja)
            dojo_data ={
                'id' : ninja_items['dojos.id'],
                'name' : ninja_items['name'],
                'created_at' : ninja_items['dojos.created_at'],
                'updated_at' : ninja_items['dojos.updated_at']
            }
            dojo_data. = Dojo(dojo_data)
            one_ninja.append()
        return ninja_items

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO ninjas ( dojo_id, first_name, last_name, age )
                VALUES ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s );
                """ #lower - values have to match html or whatever it was renamed it in the controller
                #  not necessarily here
        return connectToMySQL(db).query_db(query, data)

