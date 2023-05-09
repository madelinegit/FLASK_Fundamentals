import pymysql.cursors
#this is from a package that we installed into our app
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        #initializer is how we actually build our class in OOP
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'surfordie',
                                    db = db,
                                    charset = 'utf8mb4', #says to be in English
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = False)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    #creates and attribute and sets it to the variable that we just created
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
# a cursor is the object we use to interact with the database
                cursor.execute(query)
                #executes with the data that I just passed through
                #paused at 29mins
                #INSERT QUERY:
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                #when we run an insert query, what we get back is the ID that was just created
                # If chase was the first and only bank, then we will get back the number 1 the ID of the row
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    #here that gets everything from the database according to this query
                    #result is the variable that identifies the dictionaries that this query returns, because it is a SELECt query
                    #if it is an insert or delete query, nothing will return here
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                #If the table did not have the feild that this query tries to select, then this will print something went wrong, and e
                #e is exact;y what went wrong
                # if it didnt work the boolean will return...
                return False
            finally:
                # close the connection
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
#This is the method that calls on the MySQLConnection class, just to call on that database
#in bank_model.py this particular funciton is imported at the top of the file
