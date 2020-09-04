from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import random
import requests

#locating chromedriver to automate chrome browser
driver = webdriver.Chrome("C:/Users/grlns/Downloads/Compressed/chromedriver_win32/chromedriver")

#passing url to open in chrome browser
driver.get("https://www.cheatsheet.com/gear-style/20-questions-to-ask-siri-for-a-hilarious-response.html/")

#list to store questions
questions=[] 

content = driver.page_source
soup = BeautifulSoup(content, features='lxml')

#getting list of all questions in h2 tag
for h in soup.findAll('div', attrs={'class':'ng-binding ng-scope'}):
    if h.find('h2') != None:
        question = h.find('h2')
        questions.append(question.text)
                
#saving questions list to dataframe    
df = pd.DataFrame({'Questions':questions}) 

#converting dataframe to csv with utf-8-sig encoding to include characters as per requirement
df.to_csv('questions.csv', index=False, header=False, encoding='utf-8-sig')

#choosing random question from the list
randomQuestion = random.choice(questions)

#post request to ifttt
url = 'https://maker.ifttt.com/trigger/action_send_email/with/key/_zzJuHcSHpxrTxnaxKVuB'
postRequest = requests.post(url, json={'value1': randomQuestion})

#checking the result of request
print(postRequest.text)