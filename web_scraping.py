#The purpose of this function is to obtain the information of HTML page, in order to get the data for the database or csv file; the info is only
#for Pumas, in the future it will contain more data and maybe other teams.
#It will obtain the data from this page: https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/saison_id/2019/plus/1#MEX1
#The data to obta

import requests
import urllib.request
from bs4 import BeautifulSoup as BS

#Make a get request for the URL.
url = 'https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/plus/1?saison_id=2008'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
page = requests.get(url, headers = headers)
content = page.content
soup_Parser = BS(content,'html.parser')

#Find the element for the table, it would be the DIV element
results = soup_Parser.find_all('div', class_='responsive-table')
print(len(results))
