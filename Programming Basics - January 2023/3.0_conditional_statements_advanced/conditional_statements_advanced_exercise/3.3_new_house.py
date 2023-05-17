# read
flower_type = str(input())
flower_count = int(input())
budget = int(input())

# prices
total_price = 0
excess = 0
deficit = 0
roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

# logic
if flower_type == "Roses":
    total_price = flower_count * roses_price
    if 80 < flower_count:
        total_price = total_price - (10 / 100 * total_price)
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
    else:
        total_price = flower_count * roses_price
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
elif flower_type == "Dahlias":
    total_price = flower_count * dahlias_price
    if 90 < flower_count:
        total_price = total_price - (15 / 100 * total_price)
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
    else:
        total_price = flower_count * dahlias_price
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
elif flower_type == "Tulips":
    total_price = flower_count * tulips_price
    if 80 < flower_count:
        total_price = total_price - (15 / 100 * total_price)
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
    else:
        total_price = flower_count * tulips_price
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
elif flower_type == "Narcissus":
    total_price = flower_count * narcissus_price
    if 120 > flower_count:
        total_price = total_price + (15 / 100 * total_price)
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
    else:
        total_price = flower_count * narcissus_price
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
elif flower_type == "Gladiolus":
    total_price = flower_count * gladiolus_price
    if 80 > flower_count:
        total_price = total_price + (20 / 100 * total_price)
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
    else:
        total_price = flower_count * gladiolus_price
        if total_price <= budget:
            excess = budget - total_price
            print(f"Hey, you have a great garden with {flower_count} {flower_type} and {excess:.2f} leva left.")
        else:
            deficit = total_price - budget
            print(f"Not enough money, you need {deficit:.2f} leva more.")
else:
    print("Unknown flower! Please choose between: {Roses}, {Dahlias}, {Tulips}, {Narcissus}, or {Gladiolus}.")
