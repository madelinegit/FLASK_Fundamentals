from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app.models.models_user import User
db = 'recipesrecipes' #global variable
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

class Recipe:
    #class variable  would be here, need to say cls.db in line 36, etc, but it's outside so only needs db
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.thirtymin = data['thirtymin']
        self.instructions = data['instructions']
        self.datecreated = data['datecreated']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    # @classmethod
    # def get_one(cls, data):
    #     query = """
    #         SELECT * FROM recipes
    #         WHERE id = %(id)s;
    #         """
    #     results=connectToMySQL(db).query_db(query, data)
    #     print("results: ",results)
    #     return cls(results[0])
    @classmethod
    def get_one_chef_with_recipe(cls, data):
        query = """
            SELECT * FROM recipes
            JOIN users ON recipes.user_id = users.id
            WHERE recipes.id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query, data)
        print("get_one_chef_with_recipe results: ", results)
        chefs=[]
        # recipe = (cls, results[0])
        for user in results:
            one_chef = cls(user)
            user_data = {
                    'id' : user['users.id'], #id of the whole table(model)
                    #tried user_id same Type error
                    'firstname' : user['firstname'],
                    'lastname' : user['lastname'],
                    'email' : user['email'],
                    'password' : user['password'],
                    'created_at' : user['users.created_at'],
                    'updated_at' : user['users.updated_at']
                }
            # user_data = User(user_data)
            one_chef.cook=User(user_data)
            chefs.append(one_chef)
            print("chefs: ", chefs, "results: ", results, "cls(results[0]): ", cls(results[0]))
            # print ("results", results)
            # print("recipe" recipe)
        return cls(results[0]) #chefs

    #GET USERS WITH RECIPES
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM recipes
            JOIN users
            ON users.id = recipes.user_id
            """
        results = connectToMySQL(db).query_db(query)
        print("results", results)
        chefs=[]
        # recipe = (cls, results[0])
        for user in results:
            one_chef = cls(user)
            user_data = {
                    'id' : user['users.id'], #id of the whole table(model)
                    #tried user_id same Type error
                    'firstname' : user['firstname'],
                    'lastname' : user['lastname'],
                    'email' : user['email'],
                    'password' : user['password'],
                    'created_at' : user['users.created_at'],
                    'updated_at' : user['users.updated_at']
                }
            # user_data = User(user_data)
            one_chef.cook=User(user_data)
            chefs.append(one_chef)
            print("chefs", chefs)
        return chefs

    @classmethod
    def recipe_create (cls, newdata):
        query="""
        INSERT INTO recipes (name, description, thirtymin, instructions, datecreated, user_id)
        VALUES (%(name)s, %(description)s, %(thirtymin)s, %(instructions)s, %(datecreated)s, %(user_id)s);
        """
        return connectToMySQL(db).query_db(query,newdata)

    @classmethod
    def update (cls, form_data, id):
        query = f"UPDATE recipes SET name = %(name)s, description = %(description)s, thirtymin = %(thirtymin)s, datecreated = %(datecreated)s WHERE id={id};" #don't mention foregn key
        #%(thirtymin)s, datecreated = %(datecreated)s WHERE id={id};" #don't mention foregn key
        return connectToMySQL(db).query_db(query, form_data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @staticmethod
    def recipe_validate(recipe):
        print("recipe", recipe)
        isValid = True
        required_fields = ['name', 'description', 'instructions', 'datecreated']
        for field in required_fields:
            if field not in recipe:
                isValid=False
        # if 'thirtymin' not in recipe:
        #     recipe.thirtymin == "0"
        # recipe['thirtymin'] = recipe['thirtymin'] if 'thirtymin' in recipe else "No"
        if len(recipe['name']) < 3:
            isValid=False
            flash("Name must be at least 3 characters.")
        if len(recipe['description']) < 3:
            isValid=False
            flash("Description must be at least 3 characters.")
        if len(recipe['instructions']) < 3:
            isValid=False
            flash("Instructions must be at least 3 characters.")
        return isValid

# @staticmethod
# def recipe_validate(recipe):
#     isValid = True
#     query = "SELECT * FROM recipes WHERE name=%(name)s"
#     results = connectToMySQL(db).query_db(query, recipe)
#     if len(results)>=1:
#         isValid=False
#         flash("Recipe name already in use. Please choose a different name! Thank you.")
#     if len(recipe['name']) < 3:
#         isValid=False
#         flash("Name must be at least 3 characters.")
#     if len(recipe['description']) < 3:
#         isValid=False
#         flash("Description must be at least 3 characters.")
#     if len(recipe['instructions']) < 3:
#         isValid=False
#         flash("Instructions must be at least 3 characters.")
#     return isValid

