#Gavin Kay
#Basic Webscraper to retrieve data on top 10,000 Valorant players.
#https://github.com/GavinKay/Valorant-Scraper/blob/main/Valorant-Scraper.ipynb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import os
#open data files
nametags = open('top_10k_nametags', 'rb')
output = open('Valorant_Top10k_Stats', 'ab')

#initialize driver
driver = webdriver.Edge()


#changes IP via nordVPN
num_profiles_scraped = 0
def changeIP():
    num_profiles_scraped = num_profiles_scraped + 1
    if(num_profiles_scraped > 5):
        current = os.getcwd() #get working directory
        os.chdir("C:\\Program Files\\NordVPN") #cd into nord directory
        os.system("nordvpn -c -g 'United States'") #change ip
        os.chdir(current) #cd back into working directory
        num_profiles_scraped = 0
        time.sleep(5)
    

#scrapes player statistics from their specific webpage
def GetStats(url):
    driver.get(url)
    numbers = driver.find_elements(By.CLASS_NAME, "numbers")
    
    #write to output
    output.write(nametag + b'\n' + url.encode('iso-8859-1'))
    for n in numbers: 
        value = n.text.split('\n')[1].strip()
        output.write(value.encode('iso-8859-1') + b' : ')
    output.flush()

while(True):
    #check for EOF
    nametag = nametags.readline()
    if(nametag == ""):
        break

    #split name and tagline at #
    sts = nametag.decode('iso-8859-1').split('#')
    name = sts[0]
    tag = sts[1]

    #format name and tagline for url
    name = name.replace(' ', '%20')
    tag = tag.replace('\n', '')

    #get url for player
    url = 'https://tracker.gg/valorant/profile/riot/' + name + '%23' + tag + '/overview'
    print(url + '\n')

    #scrape data from url
    GetStats(url)
    changeIP()


output.close()



#Table of player stat values in numbers index starting at 0
#Gun1 kills             0
#Gun2 kills             1
#Gun3 kills             2
#Damage/Round           3
#K/D                    4
#HS %                   5
#Win %                  6
#Wins                   7
#KAST % per round       8
#AVG DAMAGE DEALT       9
#Kills                  10
#Deaths                 11
#Assists                12
#Average Combat Score   13
#KAD ratio              14
#kills/round            15
#first bloods           16
#flawless rounds        17
#aces                   18