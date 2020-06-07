#Crate a function to generate the HTML files for each season,
#this means obtain the info and create the HTML.
#This HTML files will contain the tables with the information.


from obtain_html_pages import obtain_html_pages_info as OBH
from obtain_info import obtain_info_from_sections as OBT
from tqdm.auto import tqdm
import os.path

class generate_html_files:

    #The __init__ funtion is the constructor of the class, what does it mean?
    #It means that every time you do a intance of the class it will begin with this function
    def __init__(self):
        #Make the call to the function to make the request to the url(s) and generate the HTML files.
        self.html_Content = OBH()
        self.section = OBT()
    
    def create_Files(self, start_year : int, end_year : int):
        #This for will obtain the information for every season of pumas, from 2010 to 2020, 
        print("Process to obtain the HTML files:")

        for i in tqdm(range(start_year, end_year)):
            print("", end='\r')

            if os.path.isfile("Results_page_Content" + str(i) + ".html"):
                #print("File exist")

                #After we have the local files que need to work with them
                self.results_Local = self.html_Content.get_Local_Content(str(i)).find_all('div', class_='responsive-table')
                for i in range(int(len(self.results_Local))):
                    self.results_Local[1].find_all('td', class_='zentriert hauptlink')
                    for y in range(int(len(self.results_Local))):
                        print(y)

                #Call the function to obtain the info from from pages
                self.section.obtain_Home_Team_Name(self.results_Local)
                self.section.obtain_Vistit_Team_Name(self.results_Local)
                self.section.obtain_Game_Plan(self.results_Local)
                self.section.obtain_Coach(self.results_Local)
                self.section.obtain_Score(self.results_Local)
                self.section.obtainAllInfo(self.results_Local)

            else:
                #print("File does not exist")
                
                #Find the element for the table, it would be the DIV element
                self.results = self.html_Content.get_Content(str(i)).find_all('div', class_='responsive-table')
        
                #Created a HTML file with the results from the results, this results have the table with the info
                create_file = open('Results_Page_Content'+ str(i) + '.html', 'w')
                create_file.write(str(self.results))
                create_file.close()
                #Call the function to obtain the info from the pages
                self.section.obtain_Date(self.results) 
                self.section.obtain_Time(self.results)
                self.section.obtain_Home_Team_Name(self.results)
                self.section.obtain_Vistit_Team_Name(self.results)
                self.section.obtain_Game_Plan(self.results)
                self.section.obtain_Coach(self.results)
                self.section.obtain_Score(self.results)
