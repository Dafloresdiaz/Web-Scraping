#The purpose of this function is to obtain the information of HTML page, in order to get the data for the database or csv file; the info is only
#for Pumas, in the future it will contain more data and maybe other teams.
#It will obtain the data from this page: https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/saison_id/2019/plus/1#MEX1
#The data will have the necessary information to have/show metrics about the team.

import requests
import urllib.request
from bs4 import BeautifulSoup as BS

#Make a get request for the URL.
url = 'https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/plus/1?saison_id=2010'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
page = requests.get(url, headers = headers)
content = page.content
soup_Parser = BS(content,'html.parser')

#Find the element for the table, it would be the DIV element
results = soup_Parser.find_all('div', class_='responsive-table')

#Created a HTML file with the results from the page. I suggest to change this functionality to another file to have this functionality separete from the
#principal objetive of this.
# In the future i think is important to have this function and work with a local file for the page, in order to avoid a lot of request to the page, the page should be
# only request one time so i think a good idea is to save onle the necessary information in a html file local and with this work.  THE POINT IS NOT TRYING TO CALL
# A LOT OF TIMES THE SAME PAGE, WE CAN BE BANNED FOR DO A OF REQUESTS.

create_file = open('Results_Page_Content.html', 'w')
create_file.write(str(results))
create_file.close()


#The table can be read it by manual calculation, if you go to the table.html, the td where the data is storage the posistion is updated by 7
#With this code you can obtain the date of the game, the range is the next one 1..8..15 etc
table_1 = results[0].find_all('td', class_='zentriert')
text = table_1[1].getText()

#With this code we need to obtain the time
table_2 = results[0].find_all('td', class_='zentriert')
text = table_2[9].getText()
#With this code we can obtain the Home team
table_3 = results[0].find_all('td', class_='zentriert')
text = table_3[3].getText()
print(text)