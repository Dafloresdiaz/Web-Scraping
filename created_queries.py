#This file is to control the queries created to insert the data in the database and also to make consults
#The only purpose of this is to create the queries and give the data in a simple way or easy way to understand

from connection_db import connection_to_database as CTDB

class create_queries:

    def __init__(self):
        self.db = CTDB()
        self.connection = self.db.create_Connection()
        self.querie = self.connection.cursor()

    def insert_coaches(self, coachName):
        self.querie.execute("SELECT COUNT(*) FROM coaches WHERE coach_Name = '%s'" % (coachName))
        result = self.querie.fetchone()[0]
        if result == 0:
            self.querie.execute("INSERT INTO coaches(coach_Name) VALUES('%s')" % (coachName))
            self.connection.commit()
    
    def insert_teams(self, teamName):
        self.querie.execute("SELECT COUNT(*) FROM teams WHERE team_Name = '%s'" % (teamName))
        result = self.querie.fetchone()[0]
        if result == 0:
            self.querie.execute("INSERT INTO teams(team_Name) VALUES('%s')" % (teamName))
            self.connection.commit()

    def insert_game_plan(self, planStrategy):
        self.querie.execute("SELECT COUNT(*) FROM game_plan WHERE gamePlan = '%s'" % (planStrategy))
        result = self.querie.fetchone()[0]
        if result == 0:
            self.querie.execute("INSERT INTO game_plan(gamePlan) VALUES('%s')" % (planStrategy))
            self.connection.commit()
