import math
# read
name = str(input())
allowance = float(input())
number_of_beers = int(input())
number_of_chips = int(input())

# calculations
price_for_beer = 1.20
beer_total = number_of_beers * price_for_beer

price_for_chips = (45 * beer_total / 100)
chips_total = math.ceil(number_of_chips * price_for_chips)

expenses = beer_total + chips_total

# logic
if expenses <= allowance:
    excess = allowance - expenses
    print(f"{name} bought a snack and has {excess:.2f} leva left.")
else:
    deficit = abs(allowance - expenses)
    print(f"{name} needs {deficit:.2f} more leva!")
