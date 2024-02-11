

print("                                             WORLD MENS T2Oi WORLD CUP 2021 POINTS TABLE")
Team1= "INDIA       "
No_of_matches_played = 5
No_of_matches_won = 3
No_of_matches_lost = No_of_matches_played - No_of_matches_won 
Total_points = No_of_matches_won*2
NRR=1.619
INDIA=[Team1, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points, NRR]
    
Team2= "PAKISTAN"
No_of_matches_played = 5
No_of_matches_won = 5
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=1.065
PAKISTAN=[Team2, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team3= "NEW ZEALAND"
No_of_matches_played = 5
No_of_matches_won = 4
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=1.277
NEW_ZEALAND=[Team3, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team4= "AFGANISTAN"
No_of_matches_played = 5
No_of_matches_won = 2
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=1.481
AFGANISTAN=[Team4, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team5= "NAMIBIA"
No_of_matches_played = 5
No_of_matches_won = 1
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=-1.851
NAMIBIA=[Team5, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team6= "SCOTLAND"
No_of_matches_played = 5
No_of_matches_won = 0
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=-3.494
SCOTLAND=[Team6, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

teams = ['INDIA', 'PAKISTAN', 'NEW_ZEALAND', 'AFGANISTAN', 'NAMIBIA', 'SCOTLAND']

points=[INDIA[-2], PAKISTAN[-2], NEW_ZEALAND[-2], AFGANISTAN[-2], NAMIBIA[-2], SCOTLAND[-2]]
NRR=[INDIA[-1], PAKISTAN[-1], NEW_ZEALAND[-1], AFGANISTAN[-1], NAMIBIA[-1], SCOTLAND[-1]]
max(points)
max(NRR)

if max(points)==INDIA[-2] :
    TEAM1= INDIA
elif max(points)==PAKISTAN[-2] :
    TEAM1=PAKISTAN
elif max(points)==NEW_ZEALAND[-2] :
    TEAM1=NEW_ZEALAND
elif max(points)==AFGANISTAN[-2]:
    TEAM1=AFGANISTAN
elif max(points)==NAMIBIA[-2]:
    TEAM1=NAMIBIA
else:
    TEAM1=SCOTLAND
    
points=[INDIA[-2], PAKISTAN[-2], NEW_ZEALAND[-2], AFGANISTAN[-2], NAMIBIA[-2], SCOTLAND[-2]]
NRR=[INDIA[-1], PAKISTAN[-1], NEW_ZEALAND[-1], AFGANISTAN[-1], NAMIBIA[-1], SCOTLAND[-1]]
points.sort(reverse=True)
NRR.sort(reverse=True)

if points[1]==INDIA[-2]:
    TEAM2= INDIA
elif points[1]==PAKISTAN[-2] :
    TEAM2=PAKISTAN
elif points[1]==NEW_ZEALAND[-2] :
    TEAM2=NEW_ZEALAND
elif points[1]==AFGANISTAN[-2] :
    TEAM2=AFGANISTAN
elif points[1]==NAMIBIA[-2] :
    TEAM2=NAMIBIA
else:
    TEAM2=SCOTLAND

if points[2]==INDIA[-2] :
    TEAM3= INDIA
elif points[2]==PAKISTAN[-2]:
    TEAM3=PAKISTAN
elif points[2]==NEW_ZEALAND[-2]:
    TEAM3=NEW_ZEALAND
elif points[2]==AFGANISTAN[-2] :
    TEAM3=AFGANISTAN
elif points[2]==NAMIBIA[-2]:
    TEAM3=NAMIBIA
else:
    TEAM3=SCOTLAND

if points[3]==INDIA[-2]:
    TEAM4= INDIA
elif points[3]==PAKISTAN[-2]:
    TEAM4=PAKISTAN
elif points[3]==NEW_ZEALAND[-2]:
    TEAM4=NEW_ZEALAND
elif points[3]==AFGANISTAN[-2]:
    TEAM4=AFGANISTAN
elif points[3]==NAMIBIA[-2] :
    TEAM4=NAMIBIA
else:
    TEAM4=SCOTLAND

if points[4]==INDIA[-2]:
    TEAM5= INDIA
elif points[4]==PAKISTAN[-2]:
    TEAM5=PAKISTAN
elif points[4]==NEW_ZEALAND[-2]:
    TEAM5=NEW_ZEALAND
elif points[4]==AFGANISTAN[-2] :
    TEAM5=AFGANISTAN
elif points[4]==NAMIBIA[-2]  :
    TEAM5=NAMIBIA
else:
    TEAM5=SCOTLAND

if points[5]==INDIA[-2] :
    TEAM6= INDIA
elif points[5]==PAKISTAN[-2] :
    TEAM6=PAKISTAN
elif points[5]==NEW_ZEALAND[-2]  :
    TEAM6=NEW_ZEALAND
elif points[5]==AFGANISTAN[-2] :
    TEAM6=AFGANISTAN
elif points[5]==NAMIBIA[-2]  :
    TEAM6=NAMIBIA
else:
    TEAM6=SCOTLAND

team_name=[]
team_name.append(TEAM1[0])
team_name.append(TEAM2[0])
team_name.append(TEAM3[0])
team_name.append(TEAM4[0])
team_name.append(TEAM5[0])
team_name.append(TEAM6[0])

match_played=[]
match_played.append(TEAM1[1])
match_played.append(TEAM2[1])
match_played.append(TEAM3[1])
match_played.append(TEAM4[1])
match_played.append(TEAM5[1])
match_played.append(TEAM6[1])

match_won=[]
match_won.append(TEAM1[2])
match_won.append(TEAM2[2])
match_won.append(TEAM3[2])
match_won.append(TEAM4[2])
match_won.append(TEAM5[2])
match_won.append(TEAM6[2])

match_lost=[]
match_lost.append(TEAM1[3])
match_lost.append(TEAM2[3])
match_lost.append(TEAM3[3])
match_lost.append(TEAM4[3])
match_lost.append(TEAM5[3])
match_lost.append(TEAM6[3])

total_points=[]
total_points.append(TEAM1[4])
total_points.append(TEAM2[4])
total_points.append(TEAM3[4])
total_points.append(TEAM4[4])
total_points.append(TEAM5[4])
total_points.append(TEAM6[4])

nnr=[]
nnr.append(TEAM1[5])
nnr.append(TEAM2[5])
nnr.append(TEAM3[5])
nnr.append(TEAM4[5])
nnr.append(TEAM5[5])
nnr.append(TEAM6[5])









Team7= "ENGLAND      "
No_of_matches_played = 5
No_of_matches_won = 5
No_of_matches_lost = No_of_matches_played - No_of_matches_won 
Total_points = No_of_matches_won*2
NRR=2.464
ENGLAND=[Team7, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points, NRR]
    
Team8 = "AUSTRALIA"
No_of_matches_played = 5
No_of_matches_won = 4
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=1.216
AUSTRALIA=[Team8, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team9= "SOUTH AFRICA"
No_of_matches_played = 5
No_of_matches_won = 3
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=0.739
SOUTH_AFRICA=[Team9, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team10= "SRI LANKA"
No_of_matches_played = 5
No_of_matches_won = 2
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=-0.269
SRILANKA=[Team10, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team11= "WEST INDIES"
No_of_matches_played = 5
No_of_matches_won = 1
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=-1.641
WESTINDIES=[Team11, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

Team12= "BANGLADESH"
No_of_matches_played = 5
No_of_matches_won = 0
No_of_matches_lost = No_of_matches_played - No_of_matches_won
Total_points = No_of_matches_won*2
NRR=-2.383
BANGLADESH=[Team12, No_of_matches_played, No_of_matches_won, No_of_matches_lost, Total_points,NRR]

teams1 = ['ENGLAND', 'AUSTRALIA', 'SOUTH AFRICA', 'SRILANKA', 'WEST INDIES', 'BANGLADESH']

points1=[ENGLAND[-2], AUSTRALIA[-2], SOUTH_AFRICA[-2], SRILANKA[-2], WESTINDIES[-2], BANGLADESH[-2]]

max(points1)

if max(points1)==ENGLAND[-2] :
    TEAM7= ENGLAND
elif max(points1)==AUSTRALIA[-2] :
    TEAM7=AUSTRALIA
elif max(points1)==SRILANKA[-2] :
    TEAM7=SRILANKA
elif max(points1)==WESTINDIES[-2]:
    TEAM7=WESTINDIES
elif max(points1)==SOUTH_AFRICA[-2]:
    TEAM7=SOUTH_AFRICA
else:
    TEAM7=BANGLADESH
    
points1=[ENGLAND[-2], AUSTRALIA[-2], SRILANKA[-2], WESTINDIES[-2], SOUTH_AFRICA[-2], BANGLADESH[-2]]
NRR1=[ENGLAND[-1], AUSTRALIA[-1], SRILANKA[-1], WESTINDIES[-1], SOUTH_AFRICA[-1], BANGLADESH[-1]]
points1.sort(reverse=True)
NRR1.sort(reverse=True)

if points1[1]==ENGLAND[-2]:
    TEAM8= ENGLAND
elif points1[1]==AUSTRALIA[-2] :
    TEAM8=AUSTRALIA
elif points1[1]==SRILANKA[-2] :
    TEAM8=SRILANKA
elif points1[1]==WESTINDIES[-2] :
    TEAM8=WESTINDIES
elif points1[1]==SOUTH_AFRICA[-2] :
    TEAM8=SOUTH_AFRICA
else:
    TEAM8=BANGLADESH

if points1[2]==ENGLAND[-2] :
    TEAM9= ENGLAND
elif points1[2]==AUSTRALIA[-2]:
    TEAM9=AUSTRALIA
elif points1[2]==SRILANKA[-2]:
    TEAM9=SRILANKA
elif points1[2]==WESTINDIES[-2] :
    TEAM9=WESTINDIES
elif points1[2]==SOUTH_AFRICA[-2]:
    TEAM9=SOUTH_AFRICA
else:
    TEAM9=BANGLADESH

if points1[3]==ENGLAND[-2]:
    TEAM10= ENGLAND
elif points1[3]==AUSTRALIA[-2]:
    TEAM10=AUSTRALIA
elif points1[3]==SRILANKA[-2]:
    TEAM10=SRILANKA
elif points1[3]==WESTINDIES[-2]:
    TEAM10=WESTINDIES
elif points1[3]==SOUTH_AFRICA[-2] :
    TEAM10=SOUTH_AFRICA
else:
    TEAM10=BANGLADESH

if points1[4]==ENGLAND[-2]:
    TEAM11= ENGLAND
elif points1[4]==AUSTRALIA[-2]:
    TEAM11=AUSTRALIA
elif points1[4]==SRILANKA[-2]:
    TEAM11=SRILANKA
elif points1[4]==WESTINDIES[-2] :
    TEAM11=WESTINDIES
elif points1[4]==SOUTH_AFRICA[-2]  :
    TEAM11=SOUTH_AFRICA
else:
    TEAM11=BANGLADESH

if points1[5]==ENGLAND[-2] :
    TEAM12= ENGLAND
elif points1[5]==AUSTRALIA[-2] :
    TEAM12=AUSTRALIA
elif points1[5]==SRILANKA[-2]  :
    TEAM12=SRILANKA
elif points1[5]==WESTINDIES[-2] :
    TEAM12=WESTINDIES
elif points1[5]==SOUTH_AFRICA[-2]  :
    TEAM12=SOUTH_AFRICA
else:
    TEAM12=BANGLADESH

team_name1=[]
team_name1.append(TEAM7[0])
team_name1.append(TEAM8[0])
team_name1.append(TEAM9[0])
team_name1.append(TEAM10[0])
team_name1.append(TEAM11[0])
team_name1.append(TEAM12[0])


match_played1=[]
match_played1.append(TEAM7[1])
match_played1.append(TEAM8[1])
match_played1.append(TEAM9[1])
match_played1.append(TEAM10[1])
match_played1.append(TEAM11[1])
match_played1.append(TEAM12[1])

match_won1=[]
match_won1.append(TEAM7[2])
match_won1.append(TEAM8[2])
match_won1.append(TEAM9[2])
match_won1.append(TEAM10[2])
match_won1.append(TEAM11[2])
match_won1.append(TEAM12[2])

match_lost1=[]
match_lost1.append(TEAM7[3])
match_lost1.append(TEAM8[3])
match_lost1.append(TEAM9[3])
match_lost1.append(TEAM10[3])
match_lost1.append(TEAM11[3])
match_lost1.append(TEAM12[3])

total_points1=[]
total_points1.append(TEAM7[4])
total_points1.append(TEAM8[4])
total_points1.append(TEAM9[4])
total_points1.append(TEAM10[4])
total_points1.append(TEAM11[4])
total_points1.append(TEAM12[4])

nnr1=[]
nnr1.append(TEAM7[5])
nnr1.append(TEAM8[5])
nnr1.append(TEAM9[5])
nnr1.append(TEAM10[5])
nnr1.append(TEAM11[5])
nnr1.append(TEAM12[5])


print('                                                                                     GROUP-1                                                                                                          ')
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("       TEAM NAME               MATCHES PLAYED           MATCHES WON          MATCHES LOST          TOTAL POINTS            NRR      ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")

for i in range( len(teams)):
    print(team_name1[i],'\t\t', match_played1[i],'\t\t\t', match_won1[i], '\t\t', match_lost1[i], '\t\t', total_points1[i], '\t\t', nnr1[i])




print("--------------------------------------------------------------------------------------------------------------------------------------------------")

print()




print('                                                                                     GROUP-2                                                                                                          ')
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("       TEAM NAME               MATCHES PLAYED           MATCHES WON          MATCHES LOST          TOTAL POINTS            NRR      ")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")

for i in range( len(teams)):
    print(team_name[i],'\t\t', match_played[i],'\t\t\t', match_won[i], '\t\t', match_lost[i], '\t\t', total_points[i], '\t\t', nnr[i])




print("--------------------------------------------------------------------------------------------------------------------------------------------------")



print()
print()
print('WAY TO PLAYOFFS:')
print()
print('FIXTURES:')
print("'THE  SEMI-FINALS'")
print("SEMI-FINAL 1:", TEAM7[0], 'VS',  TEAM2[0] )
print()
print("SEMI-FINAL 2 :", TEAM8[0], 'VS', TEAM1[0])
print()
print('THE FINALS: WINNER OF SEMI-FINAL 1  VS  WINNER OF SEMI-FINAL 2')
