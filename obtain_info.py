#The purpose of this function is to obtain the info from the html pages.
#In this case we can obtain the info from the pages like, date, time of the match,
#Home team, Visitors team and the results
#The main goal is to obtain the correct info from the html page


class obtain_info_from_sections:

    def __init__(self):
        self.x = 1
        self.y = 2

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
                    #print(self.text)
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
                    print(self.text_Time)
                    self.y = self.y + 7
                else:
                    break


