import requests
from bs4 import BeautifulSoup

url = 'https://www.ncaa.com/scoreboard/basketball-men/d1/2024/03/01/all-conf'
full = requests.get(url)
soup = BeautifulSoup(full.text, 'html.parser')
teams = soup.find_all('span', class_='gamePod-game-team-name')
scores = soup.find_all('span', class_='gamePod-game-team-score')
for i in range(len(teams)):
    print(teams[i].text)
    print(scores[i].text)