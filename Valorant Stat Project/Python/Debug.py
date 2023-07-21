#Gavin Kay 2023
from selenium import webdriver
from selenium.webdriver.common.by import By
#ENCODE EVERYTHING AS iso-8859-1
#SO VSCODE CAN PROPERLY DISPLAY CHARACTERS
#print("ä¸å®".encode('iso-8859-1'))

#edge_options = webdriver.EdgeOptions()
#edge_options.add_argument("--remote-allow-origins=*")
driver = webdriver.Edge()
driver.get(url="https://tracker.gg/valorant/profile/riot/nabil%23jess/overview")
driver.implicitly_wait(1)
numbers = driver.find_elements(By.CLASS_NAME, "numbers")
for n in numbers: 
    value = n.text.split('\n')[1]
    print(value + '\n')