#Crate a function to generate the HTML files for each season,
#this means obtain the info and create the HTML.
#This HTML files will contain the tables with the information.


from obtain_html_pages import obtain_html_pages_info as OBH
from obtain_info import obtain_info_from_sections as OBT
from tqdm.auto import tqdm

class generate_html_files:

    #The __init__ funtion is the constructor of the class, what does it mean?
    #It means that every time you do a intance of the class it will begin with this function
    def __init__(self):
        #Make the call to the function to make the request to the url(s) and generate the HTML files.
        self.html_Content = OBH()
        self.section = OBT()
    
    def create_Files(self, start_year : int, end_year : int):
        #This for will obtain the information for every season of pumas, from 2010 to 2020, 
        for i in tqdm(range(start_year, end_year)):

            #TODO Create a progress bar to know the fucntion just finish the creation of the files.

            #Find the element for the table, it would be the DIV element
            self.results = self.html_Content.get_Content(str(i)).find_all('div', class_='responsive-table')
    
            #Created a HTML file with the results from the results, this results have the table with the info
            create_file = open('Results_Page_Content'+ str(i) + '.html', 'w')
            create_file.write(str(self.results))
            create_file.close()
            print("Process to obtain the HTML files:")
            print("", end='\r')

            #Call the function to obtain the info from the pages
            self.section.obtain_time(self.results)
