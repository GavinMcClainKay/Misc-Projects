#Gavin Kay 2023
#Basic Webscraper to retrieve data on US Tax Code

from bs4 import BeautifulSoup
import requests

url = "https://www.law.cornell.edu/uscode/text/26/"
filelocation = "./US_Tax_Code.txt"

def ScrapeDocs():
    file = open(file= filelocation, mode= "a", encoding= "utf-8")
    #loop through all sections of US Tax Code and perform a request on every possible one.
    for section in range(1, 9835) :
        section_url = url + str(section)
        page = requests.get(section_url)

        #determine if the request was successful, if not, continue to the next section.
        if(page.status_code not in range(200, 300)) :
            print("Could not open section " + str(section) + " status code: " + str(page.status_code))
            page.close()
            continue
        file.writelines("\n\n SECTION: " + str(section) + "\n\n")

        #use html parser to parse div.class = "section" (class which contains all information about the tax code) 
        #and h1.class = "title" (class which contains US Tax Code title)
        soup = BeautifulSoup(page.text, "html.parser")
        title = soup.find("title")
        file.writelines(title.text + "\n")

        section_text = soup.find("div", "section").get_text(separator= "\n", strip= True)
        file.writelines(section_text)
        page.close()
        
    print("Done Scraping.")
    file.close()

ScrapeDocs()






##https://www.law.cornell.edu/uscode/text/26
##  .tocitem...
##  class .section