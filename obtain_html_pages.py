#The purpose of this funciton is to obtain all the HTML pages of Pumas in the request page
#It will help to obtain the data and save it locally (HTML File) and prevent to be baned for 
#Doing a lot of requests.

import requests
import urllib.request
from bs4 import BeautifulSoup as BS

class obtain_html_pages_info:

    def __init__(self):
        self.url = 'https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/plus/1?saison_id=2010'

    def get_Content(self):
        
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

        #Make the request to the URL
        self.page = requests.get(self.url, headers = self.headers)
        self.content = self.page.content
        self.soup_Parser = BS(self.content, 'html.parser')
        
        return self.soup_Parser