import requests
import numpy
import copy
from bs4 import BeautifulSoup

def get_team_rankings(y1, y2, d1, d2, gender):
    # Get array of team names (currently 362 of them)
    url = 'https://www.ncaa.com/standings/basketball-' + gender + '/d1'
    full = requests.get(url)
    soup = BeautifulSoup(full.text, 'html.parser')
    team_names = soup.find_all('td', class_='standings-team')
    team_names_text = []
    for name in team_names:
        team_names_text.append(name.text)

    # 28 days - 02
    # 30 days - 11
    # 31 days - 12, 01, 03
    years = [y1, y2]
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
                    if m == '11' and (int(d) > 30 or int(d) < int(d1)) or (m == '02' and int(d) > 28) or (m == '03' and int(d) > int(d2)):
                        continue
                    else:
                        url = 'https://www.ncaa.com/scoreboard/basketball-' + gender + '/d1/' + y + '/' + m + '/' + d + '/all-conf'
                        full = requests.get(url)
                        soup = BeautifulSoup(full.text, 'html.parser')
                        teams = soup.find_all('span', class_='gamePod-game-team-name')
                        scores = soup.find_all('span', class_='gamePod-game-team-score')
                        for i in range(0, len(teams), 2):
                            # if teams aren't in the list of all basketball teams, they probably
                            # weren't that important and won't be involved in the tournament
                            try:
                                idx_1 = team_names_text.index(teams[i].text)
                            except ValueError:
                                continue
                            
                            # handle empty scores
                            try:
                                score_1 = int(scores[i].text)
                            except ValueError:
                                continue
                            
                            try:
                                idx_2 = team_names_text.index(teams[i + 1].text)
                            except ValueError:
                                continue
                            
                            try:
                                score_2 = int(scores[i + 1].text)
                            except ValueError:
                                continue
                                
                            row = numpy.zeros(len(team_names))
                            row[idx_1] = 1
                            row[idx_2] = -1
                            diff = score_1 - score_2
                            if mat_A.size == 0:
                                mat_A = row
                            else:
                                mat_A = numpy.vstack((mat_A, row))
                            vec_p = numpy.append(vec_p, diff)
                        print(y + '/' + m + '/' + d)
    
    # evaluate data to solve for r                       
    mat_AT = numpy.transpose(mat_A)
    mat_ATA = numpy.matmul(mat_AT, mat_A)
    vec_ATp = mat_AT.dot(vec_p)
    mat_ATA[len(mat_ATA) - 1] = numpy.ones(len(team_names))
    vec_ATp[len(vec_ATp) - 1] = 0
    vec_r = numpy.linalg.lstsq(mat_ATA, vec_ATp,rcond=None)

    vec_r = vec_r[0].tolist()
    vec_r_sorted = copy.deepcopy(vec_r) #need deep copy to leave vec_r unsorted
    vec_r_sorted.sort(reverse=True)
    teams_sorted = []
    for i in range(len(vec_r_sorted)):
        idx = vec_r.index(vec_r_sorted[i])
        teams_sorted.append(team_names_text[idx])
        
    with open(y1 + '_' + y2 + '_' + gender + '_rankings.txt', 'w+') as f:
        for t in teams_sorted:
            f.write('%s\n' %t)
        
    f.close
            
    return teams_sorted

def team_compare(t1, t2, gender):
    file1 = open(gender + '_rankings.txt', 'r')
    rankings = []
    for t in file1.readlines():
        rankings.append(t.replace("\n", ""))
    file1.close()
     
    r1 = rankings.index(t1)
    r2 = rankings.index(t2)
    # lower number seed is better
    if r1 > r2:
        return t2
    else:
        return t1