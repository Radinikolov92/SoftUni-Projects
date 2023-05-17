import math
# read
days_away = int(input())
food_left_kg = int(input())
daily_dog_food_kg = float(input())
daily_cat_food_kg = float(input())
daily_turtle_food_gr = float(input())

# logic
dog_food_consumed = daily_dog_food_kg * days_away
cat_food_consumed = daily_cat_food_kg * days_away
turtle_food_consumed = (daily_turtle_food_gr * days_away) / 1000
total_food_consumed_for_time_period = dog_food_consumed + cat_food_consumed + turtle_food_consumed

if food_left_kg >= total_food_consumed_for_time_period:
    excess = food_left_kg - total_food_consumed_for_time_period
    print(f"{math.floor(excess)} kilos of food left.")
else:
    deficit = total_food_consumed_for_time_period - food_left_kg
    print(f"{math.ceil(deficit)} more kilos of food are needed.")
