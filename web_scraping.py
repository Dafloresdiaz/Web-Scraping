#The purpose of this function is to obtain the information of HTML page, in order to get the data for the database or csv file; the info is only, this will be at this moment in google drive
#for Pumas, in the future it will contain more data and maybe other teams.
#It will obtain the data from this page: https://www.transfermarkt.com/unam-pumas/spielplan/verein/7633/saison_id/2019/plus/1#MEX1
#The data will have the necessary information to have/show metrics about the team.
#! IMPORTANT: This main file will just call the functions

from generate_html_files import generate_html_files as CF

#*You need to have a variable to create the object and this object will have the fields
#Call the funtion to obtain the HTML files, the attributes are the years(start year and end year) for the season.
generate_Files = CF()

generate_Files.create_Files(2010, 2020)
