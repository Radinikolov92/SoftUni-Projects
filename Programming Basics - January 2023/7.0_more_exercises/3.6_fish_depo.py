# read
atlantic_mackerel_price = float(input())  # скумрия
sprinkle_price = float(input())  # цаца
bonito_kg = float(input())  # паламуд
atlantic_Horse_Mackerel_kg = float(input())  # сафрид
blue_Mussel_kg = float(input())  # миди

# read prices
bonito_price = atlantic_mackerel_price + (atlantic_mackerel_price * 60 / 100)
atlantic_Horse_Mackerel_price = sprinkle_price + (sprinkle_price * 80 / 100)
blue_Mussel_price = 7.50

# logic
bonito_sum = bonito_kg * bonito_price
atlantic_Horse_Mackerel_sum = atlantic_Horse_Mackerel_kg * atlantic_Horse_Mackerel_price
blue_Mussel_sum = blue_Mussel_kg * blue_Mussel_price
sum_total = bonito_sum + atlantic_Horse_Mackerel_sum + blue_Mussel_sum

# print
print(f"{sum_total:.2f}")
