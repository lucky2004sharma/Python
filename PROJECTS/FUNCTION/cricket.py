print("🏏 WELCOME TO CRICKET SCORECARD 🏏")
print("=" * 40)

team1_name = input("Enter 1st team name : ")
team2_name = input("Enter 2nd team name : ")

over = int(input("Enter the nnumber of overs : "))

team1_player1 = input("Enter 1st player name : ")
team1_p1_run1 = int(input("Enter the run made by 1st player : "))
team1_p1_ball1 = int(input("Enter the ball taken by 1st player : "))


team1_player2 = input("Enter 2nd player name : ")
team1_p2_run2 = int(input("Enter the run made by 1st player : "))
team1_p2_ball2 = int(input("Enter the ball taken by 1st player : "))


team1_player3 = input("Enter 3rd player name : ")
team1_p3_run3 = int(input("Enter the run made by 1st player : "))
team1_p3_ball3 = int(input("Enter the ball taken by 1st player : "))

total_run1 = team1_p1_run1 + team1_p2_run2 + team1_p3_run3

strike_rate_p1 = (team1_p1_run1*team1_p1_ball1)/100
strike_rate_p2 = (team1_p2_run2*team1_p2_ball2)/100
strike_rate_p3 = (team1_p3_run3*team1_p3_ball3)/100


team2_player1 = input("Enter 1st player name : ")
team2_p1_run1 = int(input("Enter the run made by 1st player : "))
team2_p1_ball1 = int(input("Enter the ball taken by 1st player : "))


team2_player2 = input("Enter 2nd player name : ")
team2_p2_run2 = int(input("Enter the run made by 1st player : "))
team2_p2_ball2 = int(input("Enter the ball taken by 1st player : "))


team2_player3 = input("Enter 3rd player name : ")
team2_p3_run3 = int(input("Enter the run made by 1st player : "))
team2_p3_ball3 = int(input("Enter the ball taken by 1st player : "))

total_run2 = team2_p1_run1 + team2_p2_run2 + team2_p3_run3

strike_rate2_p1 = (team2_p1_run1*team2_p1_ball1)/100
strike_rate2_p2 = (team2_p2_run2*team2_p2_ball2)/100
strike_rate2_p3 = (team2_p3_run3*team2_p3_ball3)/100


if total_run1 > total_run2:
    winner = team1_name
    margin = total_run1 - total_run2
    message = f"{team1_name} won against {team2_name} by {margin} run"
    
elif total_run1 < total_run2:
    winner = team2_name
    margin = total_run2 - total_run1
    message = f"{team2_name} won against {team1_name} by {margin} run"
    
else:
    winner = "Nobody"
    message = "The Match is Draw"



# all_runs  = [team1_p1_run1, team1_p2_run2, team1_p3_run3,     team2_p1_run1, team2_p2_run2, team2_p3_run3]
# all_names = [team1_player1  , team1_player2 , team1_player3,  team2_player1  , team2_player2 , team2_player3]
# all_sr    = [strike_rate_p1, strike_rate_p2, strike_rate_p3,    strike_rate2_p1, strike_rate2_p2, strike_rate2_p3]

# best_runs = max(all_runs)
# motm_index = all_runs.index(best_runs)
# motm_name  = all_names[motm_index]
# motm_sr    = all_sr[motm_index]



print(team1_name)
print(team2_name)

print(team1_player1  , team1_player2 , team1_player3)
print(team2_player1  , team2_player2 , team2_player3)
    
print(team1_p1_run1, team1_p2_run2, team1_p3_run3)
print(team2_p1_run1, team2_p2_run2, team2_p3_run3)

print(total_run1)
print(total_run2)

print(strike_rate_p1, strike_rate_p2, strike_rate_p3)
print(strike_rate2_p1, strike_rate2_p2, strike_rate2_p3)

print(winner)
print(margin)
print(message)

# print(best_runs)
# print(motm_index)
# print(motm_name)
# print(motm_sr)