# read
season = str(input())
km_month = float(input())

# logic
salary_per_km = 0
total_salary = 0
gross_income = 0
duration = 4

if 0 <= km_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary_per_km = 0.75
    elif season == "Summer":
        salary_per_km = 0.90
    elif season == "Winter":
        salary_per_km = 1.05
    else:
        print("Incorrect input! Please type in a valid season: {Spring} , {Summer} , {Autumn} or {Winter}.")
elif 5000 < km_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary_per_km = 0.95
    elif season == "Summer":
        salary_per_km = 1.10
    elif season == "Winter":
        salary_per_km = 1.25
    else:
        print("Incorrect input! Please type in a valid season: {Spring} , {Summer} , {Autumn} or {Winter}.")
elif 10000 < km_month <= 20000:
    if season == "Spring" or season == "Autumn" or season == "Summer" or season == "Winter":
        salary_per_km = 1.45
    else:
        print("Incorrect input! Please type in a valid season: {Spring} , {Summer} , {Autumn} or {Winter}.")
else:
    print("You are lazy and didn't move from home! No money for you!")

# calculations
total_salary = (km_month * salary_per_km) * duration
taxes = 10 * total_salary / 100
gross_income = total_salary - taxes

# print
print(f"{gross_income:.2f}")
