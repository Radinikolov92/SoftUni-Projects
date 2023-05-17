# read
import math
number_of_tournaments = int(input())
starter_points = int(input())

# logic
total_points = starter_points
average_for_tournaments = 0
percent_won_tournaments = 0
tournament_points = 0
won_tournaments = 0

for year in range(1, number_of_tournaments + 1):
    finish_results = str(input())
    if finish_results == "W":
        total_points += 2000
        tournament_points += 2000
        won_tournaments += 1
    elif finish_results == "F":
        total_points += 1200
        tournament_points += 1200
    elif finish_results == "SF":
        total_points += 720
        tournament_points += 720
    else:
        print("Did not classify!")

average_for_tournaments = tournament_points / number_of_tournaments
percent_won_tournaments = (won_tournaments / number_of_tournaments) * 100

# print
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_for_tournaments)}")
print(f"{percent_won_tournaments:.2f}%")
