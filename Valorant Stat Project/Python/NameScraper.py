#Gavin Kay 2023
#Basic Webscraper to retrieve data on top 10,000 Valorant players.

from bs4 import BeautifulSoup
import requests
import time

url = "https://tracker.gg/valorant/leaderboards/ranked/all/src=?page="

#Function to scrape all player names on tracker.gg top 10,000 leaderboard
def ScrapeNames(pagenum, output_file):
    #perform an html GET request on url
    page = requests.get(url + str(pagenum))

    #init parser and parse names and taglines of all players on the page
    soup = BeautifulSoup(page.text, "html.parser")
    names = soup.findAll("span", "trn-ign__username")
    tags = soup.findAll("span", "trn-ign__discriminator")

    #iterate over names and taglines to combine them (will need combined to find exact player when we parse player stats)
    for n in range(names.__len__()):
        #encode EVERYTHING as iso-8859-1 because there are alot of utf-8 characters that will not properly display on vscode
        name = names[n].text.strip().encode('iso-8859-1')
        tag = tags[n].text.strip().encode('iso-8859-1')
        output_file.write(name + tag + b"\n")
        #print(i + " " + name + tag + "\n")


print("STARTING!!")
output_file = open("top_10k_nametags", "ab")
#iterate through all 90 pages of tracker.gg top 10,000 leaderboard
for i in range(90):
    ScrapeNames(i, output_file)
    #sleep 3 seconds between each page so we do not trigger anti-ddos countermeasures (tracker.gg will not allow a certain amount of requests in an alloted time 3 sec was just a guess)
    time.sleep(3)
    
output_file.close()
print("DONE!!")