#This file is to control the queries created to insert the data in the database and also to make consults
#The only purpose of this is to create the queries and give the data in a simple way or easy way to understand

from connection_db import connection_to_database as CTDB

class create_queries:

    def __init__(self):
        self.db = CTDB()
        self.connection = self.db.create_Connection()
        self.querie = self.connection.cursor()

    def insert_coaches(self, coachName):
        #This first query is to obtain if the coacha name is already in the table
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
        wotSpaces = planStrategy.lstrip()
        wotSpaces = wotSpaces.rstrip()
        if len(wotSpaces) > 1:
            self.querie.execute("SELECT COUNT(*) FROM game_plan WHERE gamePlan = '%s'" % (wotSpaces))
            result = self.querie.fetchone()[0]
            if result == 0:
                self.querie.execute("INSERT INTO game_plan(gamePlan) VALUES('%s')" % (wotSpaces))
                self.connection.commit()

    def insert_all_info(self, homeTeam, visitTeam, score, dateTime, coach, plan):

        #Home Team ID
        self.querie.execute("SELECT id FROM teams WHERE team_Name = '%s'" % (homeTeam))
        idHomeTeam = self.querie.fetchone()[0]
        #idVisitTeam
        self.querie.execute("SELECT id FROM teams WHERE team_Name = '%s'" % (visitTeam))
        idVisitTeam = self.querie.fetchone()[0]
        #idCoaches
        if coach != None:
            self.querie.execute("SELECT id FROM coaches WHERE coach_Name = '%s' " % (coach))
            idCoach = self.querie.fetchone()[0]
        else:
            idCoach = None
        #idPlan
        if plan != '?' or plan != None:
            self.querie.execute("SELECT id FROM game_plan WHERE gamePlan = '%s' " % (plan))
            idPlan = self.querie.fetchone()[0]
        else:
            idPlan = None
            

        self.querie.execute("INSERT INTO complete_info(id_home_team, id_visit_team, score, date_time, id_coach, id_plan) VALUES('%i', '%i', '%s', '%s', '%i', '%i')" % (idHomeTeam, idVisitTeam, score, dateTime, idCoach, idPlan))
        self.connection.commit()

