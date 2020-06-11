#The purpose of this function is to obtain the info fro7m the html pages.
#In this case we can obtain the info from the pages like, date, time of the match,
#Home team, Visitors team and the results
#The main goal is to obtain the correct info from the html page

from datetime import datetime as dt
from created_queries import create_queries as CQ

class obtain_info_from_sections:

    def __init__(self):
        self.database = CQ()
        self.x = 0
        self.y = 0

#    def obtain_Date(self, results):
#        #The table can be read it by manual calculation, if you go to the *.html, the td where the 
#        #data is storage the posistion is updated by 7
#        # * With this code you can obtain the date of the game, the range is the next one 1, 8, 15
#        for i in range(int(len(results))):
#            self.date = results[i].find_all('td', class_='zentriert')
#            self.x = 1
#            for _ in range(int(len(self.date))):
#                if self.x < int(len(self.date)):
#                    self.text = self.date[self.x].getText()
#                    # ! The range is always 1 + 7 = 8 this equal to the next field
#                    self.x = self.x + 7
#                else:
#                    break
#
#    def obtain_Time(self, results):
#         #The table can be read it by manual calculation, if you go to the *.html, the td where the 
#        #data is storage the posistion is updated by 7
#        for i in range(int(len(results))):
#            self.time = results[i].find_all('td', class_='zentriert')
#            self.x = 2
#            for _ in range(int(len(self.time))):
#                if self.x < int(len(self.time)):
#                    self.text_Time = self.time[self.x].getText()
#                    self.x = self.x + 7
#                else:
#                    break
    
    #obtain the home team name
    def obtain_Home_Team_Name(self, results):
        self.x = 0
        for i in range(int(len(results))):
            self.homeTeam = results[i].find_all('a', class_='vereinprofil_tooltip')
            self.x = 1
            for _ in range(int(len(self.homeTeam))):
                if self.x < int(len(self.homeTeam)):
                    self.text_Home_Team = self.homeTeam[self.x].getText()
                    self.database.insert_teams(self.text_Home_Team)
                    self.x = self.x + 4
                else:
                    break
    
    #obtain the Away team
    def obtain_Vistit_Team_Name(self, results):
        self.x = 0
        for i in range(int(len(results))):
            self.visitTeam = results[i].find_all('a', class_='vereinprofil_tooltip')
            self.x = 3
            for _ in range(int(len(self.visitTeam))):
                if self.x < int(len(self.visitTeam)):
                    self.text_Visit_Team = self.visitTeam[self.x].getText()
                    self.database.insert_teams(self.text_Visit_Team)
                    self.x = self.x + 4
                else:
                    break

    #Obtain the Game plan
    def obtain_Game_Plan(self, results):
         self.x = 0
         for i in range(int(len(results))):
            self.gamePlan = results[i].find_all('td', class_='zentriert')
            self.x = 5
            for _ in range(int(len(self.gamePlan))):
                if self.x < int(len(self.gamePlan)):
                    self.text_Game_Plan = self.gamePlan[self.x].getText()
                    self.database.insert_game_plan(self.text_Game_Plan)
                    self.x = self.x + 7
                else:
                    break
    
    def obtain_Coach(self, results):
         self.x = 0
         for i in range(int(len(results))):
            self.coach = results[i].find_all('a', id='0')
            self.x = 0
            for _ in range(int(len(self.coach))):
                if self.x < int(len(self.coach)):
                    self.text_Coach = self.coach[self.x].getText()
                    self.database.insert_coaches(self.text_Coach)
                    self.x = self.x + 1
                else:
                    break

    def obtain_Score(self, results):
        self.x = 0
        for i in range(int(len(results))):
            self.score = results[i].find_all('a', title="Match report")
            self.x = 0
            for scoreArray in range(int(len(self.score))):
                if self.x < int(len(self.score)):
                    self.text_Score = self.score[self.x].getText()
                    self.x = self.x + 1
                else:
                    break

    def obtainAllInfo(self, results):
        self.x = 0
        self.y = 0
        positionForDateTime = 0
        positionForHomeTeam = 0
        positionForVisitTeam = 0
        listDate = []
        listHomeTeam = []
        listVisitTeam = []
        for i in range(int(len(results))):
            dateTimeTags = results[i].find_all('td', class_='zentriert')
            homeTeam = results[i].find_all('a', class_='vereinprofil_tooltip')
            visitTeam = results[i].find_all('a', class_='vereinprofil_tooltip')
            self.x = 1
            self.y = 2
            for i in range(int(len(dateTimeTags))):
                if (self.x < int(len(dateTimeTags))) and (self.y < int(len(dateTimeTags))):
                    dateTime = dateTimeTags[self.x].getText() + " " +dateTimeTags[self.y].getText()
                    dateForSQL = dt.strptime(dateTime, '%a %b %d, %Y %I:%M %p')
                    dateString = dateForSQL.strftime('%Y-%m-%d %H:%M:%S')
                    listDate.insert(positionForDateTime, dateString)
                    self.x = self.x + 7
                    self.y = self.y + 7
                    positionForDateTime += 1
                else:
                    break

            x = 1
            for i in range(int(len(homeTeam))):
                if x < int(len(homeTeam)):
                    textHome = homeTeam[x].getText()
                    listHomeTeam.insert(positionForHomeTeam, textHome)
                    x += 4
                    positionForHomeTeam += 1

            x = 3
            for i in range(int(len(visitTeam))):
                if x < int(len(visitTeam)):
                    textVisit = visitTeam[x].getText()
                    listVisitTeam.insert(positionForVisitTeam, textVisit)
                    x += 4
                    positionForVisitTeam += 1
                else:
                    break
        
        print(listVisitTeam[0])


