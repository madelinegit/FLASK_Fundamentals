#Our class may make this file plural liek friends.py and banks.py
#This way makes it harder to confuse the model with other py docs
#from mysqlconnections import MySQLConnection
#would mean, connect to the FILE

from mysqlconnection import connectToMySQL
#this means, connecto the function at the bottom of that document

#let's call OOP into our database and create class instances
#turn data into class instances before returning them back to server.py and then index.html
#that's the whole point of the OOP model to use instances to hold data and do things with it

db = "bank_app"
#makes DB in to a variable that is hard to mess up with a typo, like the database document
#you can put this into your class if you want, and refer to it as cl.db instead of just db

class Bank:
    def __init__(self, data):
        self.id = data('id')
        self.name = data['name']
        self.address = data['address']
        self.phone = data['phone']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #called on all of the rows

#now we can start creating our different methods in order to query our data base

    # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        #insert query to save data into a databse
        query = "INSERT INTO bank ( name , address, phone,created_at, updated_at ) VALUES ( %(name)s, %(address)s , %(phone)s)"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(db).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM banks"
        results = connectToMySQL(cls.db).query_db(query)
        banks = []
        for bank in results:
            bank.append(cls(bank))
        return banks

    @classmethod
    def get_one(cls,id):
        query  = "SELECT * FROM bankss WHERE id = %(id)s";
        """ data = {'id':bank_id} """
        results = connectToMySQL(cls.DB).query_db(query, {'id':id})
        return cls(results[0])
    # a get one still gives us back a list of dictionaries, it's just one dictionary though cause ID is unique)