from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='/Users/samdubois/Downloads/chromedriver')
driver.get('https://www.nba.com/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all('div', class_='Scoreboard_gameContainer__28y3Q')

for result in results :
    #title_elem = job_elem.find('h2', class_='title')
    isInGame = result.find(attrs={"data-id": "nba:game-tracker:game-matchup:link"})
    
    if isInGame.text == 'WATCH':
        print(isInGame.text)
    else:
        break

# Close Driver
driver.close()