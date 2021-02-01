from selenium import webdriver
from bs4 import BeautifulSoup

def retrieve_all_games():
    # Specify Web Driver
    driver = webdriver.Chrome(executable_path='/Users/samdubois/Downloads/chromedriver')
    driver.get('https://www.nba.com/')

    # Prepare Web Scraper
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve All Games
    results = soup.find_all('div', class_='Scoreboard_gameContainer__28y3Q')

    for result in results :
        #title_elem = job_elem.find('h2', class_='title')
        gameData = result.find(attrs={"data-id": "nba:game-tracker:game-matchup:link"})

        if gameData != None:
            # Bracket for all live games

            
            print(result.text)
        else:
            # Bracket got all games coming that day
            break

    # Close Driver
    driver.close()

retrieve_all_games()