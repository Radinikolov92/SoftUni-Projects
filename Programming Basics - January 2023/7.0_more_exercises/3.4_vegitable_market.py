# read
vegetables_price_kg = float(input())
fruits_price_kg = float(input())
vegetables_kgs = int(input())
fruits_kgs = int(input())
euro_course = 1.94

# logic
income_vegetables = vegetables_kgs * vegetables_price_kg
income_fruits = fruits_kgs * fruits_price_kg
total_income = income_vegetables + income_fruits
euro_equivalent = total_income / euro_course

# print
print(f"{euro_equivalent:.2f}")
