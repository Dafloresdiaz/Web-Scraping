#The purpose of this function is to obtain the information of HTML page, in order to get the data for the database or csv file; the info is only, this will be at this moment in google drive
#for Pumas, in the future it will contain more data and maybe other teams.
#It will obtain the data from this page: https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/saison_id/2019/plus/1#MEX1
#The data will have the necessary information to have/show metrics about the team.

import requests
import urllib.request
from bs4 import BeautifulSoup as BS
from obtain_html_pages import obtain_html_pages_info as obt

#This for will obtain the information for every season of pumas, from 2010 to 2020, 
for i in range(2010, 2021):
    #Make the call to the function to make the request to the url(s) and generate the HTML files.
    html_Content = obt()
    #Find the element for the table, it would be the DIV element
    #TODO: Make the function get_Content() has an attribute to send the year and concatane to the url
    results = html_Content.get_Content(str(i)).find_all('div', class_='responsive-table')
    #Created a HTML file with the results from the page. I suggest to change this functionality to another file to have this functionality separete from the
    #principal objetive of this.
    create_file = open('Results_Page_Content'+ str(i) + '.html', 'w')
    create_file.write(str(results))
    create_file.close()


