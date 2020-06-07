#The purpose of this function is to obtain the info from the html pages.
#In this case we can obtain the info from the pages like, date, time of the match,
#Home team, Visitors team and the results
#The main goal is to obtain the correct info from the html page

from created_queries import create_queries as CQ

class obtain_info_from_sections:

    def __init__(self):
        self.database = CQ()
        self.x = 0
        self.y = 0
        self.w = 0
        self.z = 0
        self.a = 0
        self.b = 0



    def obtain_Date(self, results):
        #The table can be read it by manual calculation, if you go to the *.html, the td where the 
        #data is storage the posistion is updated by 7
        # * With this code you can obtain the date of the game, the range is the next one 1, 8, 15
        for i in range(int(len(results))):
            self.date = results[i].find_all('td', class_='zentriert')
            self.x = 1
            for position in range(int(len(self.date))):
                if self.x < int(len(self.date)):
                    self.text = self.date[self.x].getText()
                    # ! The range is always 1 + 7 = 8 this equal to the next field
                    self.x = self.x + 7
                else:
                    break

    def obtain_Time(self, results):
         #The table can be read it by manual calculation, if you go to the *.html, the td where the 
        #data is storage the posistion is updated by 7
        for i in range(int(len(results))):
            self.time = results[i].find_all('td', class_='zentriert')
            self.y = 2
            for position in range(int(len(self.time))):
                if self.y < int(len(self.time)):
                    self.text_Time = self.time[self.y].getText()
                    self.y = self.y + 7
                else:
                    break
    
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
         for i in range(int(len(results))):
            self.coach = results[i].find_all('a', id='0')
            self.a = 0
            for _ in range(int(len(self.coach))):
                if self.a < int(len(self.coach)):
                    self.text_Coach = self.coach[self.a].getText()
                    self.database.insert_coaches(self.text_Coach)
                    self.a = self.a + 1
                else:
                    break

    def obtain_Score(self, results):
        for i in range(int(len(results))):
            self.score = results[i].find_all('a', title="Match report")
            self.b = 0
            for scoreArray in range(int(len(self.score))):
                if self.a < int(len(self.score)):
                    self.text_Score = self.score[self.a].getText()
                    self.b = self.b + 1
                else:
                    break

            





