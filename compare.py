import ranking

t1 = input("Enter team 1 to compare: ")
t2 = input("Enter team 2 to compare: ")
gender = input('Mens or womens? (M or W): ')
if gender == "M":
    gender = 'men'
else:
    gender = 'women'
best = ranking.team_compare(t1, t2, gender)
print("The better team is " + best)