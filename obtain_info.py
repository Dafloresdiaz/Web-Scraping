#The purpose of this function is to obtain the info from the html pages.
#In this case we can obtain the info from the pages like, date, time of the match,
#Home team, Visitors team and the results
#The main goal is to obtain the correct info from the html page


class obtain_info_from_sections:

    def __init__(self):
        self.x = 1

    def obtain_time(self, results):
        #The table can be read it by manual calculation, if you go to the *.html, the td where the 
        #data is storage the posistion is updated by 7
        # * With this code you can obtain the date of the game, the range is the next one 1, 8, 15
        #TODO make a for to go to every date from the html page
        for i in range(int(len(results))):
            self.time = results[i].find_all('td', class_='zentriert')
            self.x = 1
            for y in range(int(len(self.time))):
                if self.x < int(len(self.time)):
                    self.text = self.time[self.x].getText()
                    #print(self.text)
                    # ! The range is always 1 + 7 = 8 this equal to the next field
                    self.x = self.x + 7
                else:
                    break
                
            