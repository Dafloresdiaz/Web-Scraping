#The purpose of this funciton is to obtain all the HTML pages of Pumas in the request page
#It will help to obtain the data and save it locally (HTML File) and prevent to be baned for 
#Doing a lot of requests.

import requests
import urllib.request
from bs4 import BeautifulSoup as BS

class obtain_html_pages_info:

    #The __init__ funtion is the constructor of the class, what does it mean?
    #It means that every time you do a intance of the class it will begin with this function
    def __init__(self):
        self.url = 'https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/plus/1?saison_id='

    def get_Content(self, year : str):
        
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

        #Make the request to the URL
        self.page = requests.get((self.url + year), headers = self.headers)
        self.content = self.page.content
        self.soup_Parser = BS(self.content, 'html.parser')
        
        return self.soup_Parser