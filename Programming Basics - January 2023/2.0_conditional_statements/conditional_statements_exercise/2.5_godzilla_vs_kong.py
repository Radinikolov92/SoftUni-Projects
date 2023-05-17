# read
budget = float(input())
crew = int(input())
crew_clothing_price = float(input())
decor = budget * 10 / 100
clothing_discount = crew_clothing_price * 10 / 100
if crew >= 150:
    crew_clothing_price = crew_clothing_price - clothing_discount

# logic
expenses = (crew_clothing_price * crew) + decor

if expenses > budget:
    deficit = expenses - budget
    print(f"Not enough money!")
    print(f"Wingard needs {deficit:.2f} leva more.")

elif expenses <= budget:
    excess = budget - expenses
    print(f"Action!")
    print(f"Wingard starts filming with {excess:.2f} leva left.")
