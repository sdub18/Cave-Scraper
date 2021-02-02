from selenium import webdriver
from bs4 import BeautifulSoup
from constants import teamDict

# Given the URL to a live game, grab important stats from that game, including score, teams, time, and quarter.
# Will generate an error if game has concluded.
# Return in JSON format.

def getLiveGameInfo(URL):

    driver = webdriver.Chrome()

    driver.get(URL)

    html = driver.page_source

    soup = BeautifulSoup(html, features="lxml")

    scoreResults = soup.findAll("p", {"class": "h9 relative inline-block leading-none"})

    timeResults = soup.findAll("span", {"class": "ml-1"})

    quarterResults = soup.findAll("p", {"class": "flex items-center justify-center mt-1 text-xs"})

    driver.quit()

    homeTeam = teamDict[URL[25:28].upper()]
    awayTeam = teamDict[URL[32:35].upper()]

    scores = []
    for score in scoreResults:
        scores.append(score.text)
    
    homeScore = scores[0]
    awayScore = scores[1]

    time = timeResults[0].text

    quarter = quarterResults[0].text[0:2]

    output = {"homeTeam": homeTeam, "homeScore": homeScore, "awayTeam": awayTeam, "awayScore": awayScore, "timeReamining": time, "quarter": quarter}

    return output

# ------------------------------------- Test -------------------------------------

URL = "https://www.nba.com/game/phx-vs-dal-0022000319"
print(getLiveGameInfo(URL))