# read
number_of_juniors = int(input())
number_of_seniors = int(input())
track_type = str(input())

# read prices

juniors_trail_price = 5.50
seniors_trail_price = 7
juniors_cross_country_price = 8
seniors_cross_country_price = 9.50
juniors_downhill_price = 12.25
seniors_downhill_price = 13.75
juniors_road_price = 20
seniors_road_price = 21.50

# logic
tax_for_juniors = 0
tax_for_seniors = 0
gathered_sum = 0
donated_money = 0
total_number_of_contestants = number_of_juniors + number_of_seniors

if track_type == "trail":
    tax_for_juniors = number_of_juniors * juniors_trail_price
    tax_for_seniors = number_of_seniors * seniors_trail_price
    gathered_sum = tax_for_juniors + tax_for_seniors
    expenses = 5 * gathered_sum / 100
    donated_money = gathered_sum - expenses

elif track_type == "cross-country":
    tax_for_juniors = number_of_juniors * juniors_cross_country_price
    tax_for_seniors = number_of_seniors * seniors_cross_country_price
    if 50 <= total_number_of_contestants:
        tax_for_juniors = tax_for_juniors - (25 * tax_for_juniors / 100)
        tax_for_seniors = tax_for_seniors - (25 * tax_for_seniors / 100)
        gathered_sum = tax_for_juniors + tax_for_seniors
        expenses = 5 * gathered_sum / 100
        donated_money = gathered_sum - expenses
    else:
        gathered_sum = tax_for_juniors + tax_for_seniors
        expenses = 5 * gathered_sum / 100
        donated_money = gathered_sum - expenses

elif track_type == "downhill":
    tax_for_juniors = number_of_juniors * juniors_downhill_price
    tax_for_seniors = number_of_seniors * seniors_downhill_price
    gathered_sum = tax_for_juniors + tax_for_seniors
    expenses = 5 * gathered_sum / 100
    donated_money = gathered_sum - expenses

elif track_type == "road":
    tax_for_juniors = number_of_juniors * juniors_road_price
    tax_for_seniors = number_of_seniors * seniors_road_price
    gathered_sum = tax_for_juniors + tax_for_seniors
    expenses = 5 * gathered_sum / 100
    donated_money = gathered_sum - expenses

else:
    print("Incorrect track type!")

# print
print(f"{donated_money:.2f}")
