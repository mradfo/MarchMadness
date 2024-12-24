import ranking

# orders from best to worst
start_year = input('Enter the year the basketball season started in: ')
end_year = str(int(start_year) + 1)

valid_months = ['11', '12', '01', '02', '03']
start_month = input('Enter the 2 digit month you would like to begin in: ')
if not (start_month in valid_months):
    raise Exception('Invalid month')
end_month = input('Enter the 2 digit month you would like to end in: ')
if not end_month in valid_months:
    raise Exception('Invalid month')
idx_1 = valid_months.index(start_month)
idx_2 = valid_months.index(end_month)
if idx_2 < idx_1:
    raise Exception('Start month must be before end month')

start_day = input('Enter the day that you would like to start tracking from: ')
end_day = input('Enter the day you would like to end tracking: ')
gender = input('Mens or womens? (M or W): ')
if gender == "M":
    gender = 'men'
else:
    gender = 'women'
order = ranking.get_team_rankings(start_year, end_year, start_month, end_month, start_day, end_day, gender)

for i in range(0, len(order)):
    print(str(i + 1) + ". " + order[i])