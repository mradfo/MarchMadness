import requests
import numpy
from bs4 import BeautifulSoup

# Get array of team names (currently 362 of them)
url = 'https://www.ncaa.com/standings/basketball-men/d1'
full = requests.get(url)
soup = BeautifulSoup(full.text, 'html.parser')
team_names = soup.find_all('td', class_='standings-team')
print(len(team_names))
#for name in team_names:
#    print(name.text)

# 28 days - 02
# 30 days - 11
# 31 days - 12, 01, 03
years = ['2023', '2024']
months = ['11', '12', '01', '02', '03']
days = ['01', '02', '03', '04', '05', '06', '07', 
        '08', '09', '10', '11', '12', '13', '14',
        '15', '16', '17', '18', '19', '20', '21',
        '22', '23', '24', '25', '26', '27', '28',
        '29', '30', '31']
mat_A = numpy.array([])
vec_p = numpy.array([])

for y in years:
    for m in months:
        if (y == years[0] and (m == '01' or m == '02' or m == '03')) or (y == years[1] and (m == '11' or m == '12')):
            continue
        else:
            for d in days:
                if m == '11' and (int(d) > 30 or int(d) < 6) or (m == '02' and int(d) > 28) or (m == '03' and int(d) > 17):
                    continue
                else:
                    url = 'https://www.ncaa.com/scoreboard/basketball-men/d1/' + y + '/' + m + '/' + d + '/all-conf'
                    #print(url)
                    full = requests.get(url)
                    soup = BeautifulSoup(full.text, 'html.parser')
                    teams = soup.find_all('span', class_='gamePod-game-team-name')
                    scores = soup.find_all('span', class_='gamePod-game-team-score')
                    for i in range(len(teams)):
                        idx_1 = team_names.index(teams[i].text)
                        score_1 = scores[i].text
                        idx_2 = team_names.index(teams[i + 1].text)
                        score_2 = scores[i + 1].text
                        row = numpy.zeros(len(team_names))
                        if int(score_1) > int(score_2):
                            row[idx_1] = 1
                            row[idx_2] = -1
                        elif int(score_2) > int(score_1):
                            row[idx_1] = -1
                            row[idx_2] = 1
                        # what do we do in the case of a tie??
                        numpy.append(mat_A, row)
                        print(mat_A)

#for i in range(len(teams)):
#    print(teams[i].text)
#    print(scores[i].text)