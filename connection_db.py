#This class is to obtain the connection to the database only one time in the other files
import sqlite3 as sql

class connection_to_database:

    def __init__(self):
       
        try:
            self.connection = sql.connect("pumas_DB_Test.db")
        except:
            print(" Something is wrong, the connection to the Database could not be completed  :( ")
        else:
            print(" Connection to the Database is correct :) ")

    def create_Cursor(self):
        queries = self.connection.cursor()
        return queries
