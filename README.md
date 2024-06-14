# MarchMadness
Steps:
- need to know all of the participating teams and place them in some order
- go through each game in the season and determine which teams were playing, who won, and the score difference
- create matrix A and vector p with this information
- calculate ATA and ATp
- replace last row of ATA with all 1s
- replace last entry of ATp with 0
- solve ATAr = ATp for r
- r is ranking of teams in originally determined order

Notes:
- tied games are represented by a 0 in p