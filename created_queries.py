#This file is to control the queries created to insert the data in the database and also to make consults
#The only purpose of this is to create the queries and give the data in a simple way or easy way to understand

from connection_db import connection_to_database as CTDB

class create_queries:

    def __init__(self):
        connection = CTDB()