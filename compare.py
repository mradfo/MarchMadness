import ranking

t1 = input("Enter team 1 to compare: ")
t2 = input("Enter team 2 to compare: ")
file = input("Enter filename with results to use: ")
best = ranking.team_compare(t1, t2, file)
print(best + " is the better team.")