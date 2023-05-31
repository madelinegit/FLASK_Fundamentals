from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_ninja import Ninja

db = 'dojos_ninjas'

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]
        #if you add to the init after making the DB, this info will not come from DB, it will come from somewhere else, maybe the model file

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for ninjas in results:
            ninja_data ={
                'id': ninjas['ninjas.id'],
                'first_name': ninjas['first_name'],
                'last_name': ninjas['last_name'],
                'age': ninjas['age'],
                "created_at": ninjas['ninjas.created_at'],
                "updated_at": ninjas['ninjas.updated_at'],
                "dojo_id": ninjas['dojo_id']
            }
            # print(ninjas)
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(db).query_db(query)
        dojo_items = []
        for dojos in results:
            dojo_items.append(cls(dojos))
        return dojo_items

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos ( name )
                VALUES ( %(name)s );
                """
        return connectToMySQL(db).query_db(query, data)
