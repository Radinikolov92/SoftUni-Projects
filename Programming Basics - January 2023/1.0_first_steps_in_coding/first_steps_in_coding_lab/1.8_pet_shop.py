
number_of_cat_food = int(input())
number_of_dog_food = int(input())
price_of_cat_food = float(4)
price_of_dog_food = float(2.50)
expenses_for_cat_food = number_of_cat_food * price_of_cat_food
expenses_for_dog_food = number_of_dog_food * price_of_dog_food
total_expenses = float(expenses_for_cat_food + expenses_for_dog_food)
print(f"{total_expenses} lv.")