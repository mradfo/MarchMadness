import ranking

# orders from best to worst
start_year = input('Enter the year the basketball season started in: ')
end_year = str(int(start_year) + 1)
start_day = input('Enter the day in November that the regular season started: ')
end_day = input('Enter the day in March that the regular season ended: ')
order = ranking.get_team_rankings(start_year, end_year, start_day, end_day)

for i in range(0, len(order)):
    print(str(i + 1) + ". " + order[i])