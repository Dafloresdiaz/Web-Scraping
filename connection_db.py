#This class is to obtain the connection to the database only one time in the other files
import sqlite3 as sql

class connection_to_database:

    def create_Connection(self):
        try:
            connection = sql.connect("pumas_DB_Test.db")
        except:
            print("Something is wrong, the connection to the Database could not be completed  :( ")
        else:
            print("Connection to the Database is correct :) ")
            return connection