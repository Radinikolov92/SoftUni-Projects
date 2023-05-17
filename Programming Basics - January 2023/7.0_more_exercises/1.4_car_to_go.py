# read
budget = float(input())
season = str(input())

# variables
class_type = "N/A"
car_type = "N/A"
car_price = 0

# logic
if 0 <= budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 35 * budget / 100
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 65 * budget / 100
    else:
        print("Invalid season! Please choose between {Summer} and {Winter}.")
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 45 * budget / 100
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 80 * budget / 100
    else:
        print("Invalid season! Please choose between {Summer} and {Winter}.")
elif 500 < budget:
    class_type = "Luxury class"
    if season == "Summer" or season == "Winter":
        car_type = "Jeep"
        car_price = 90 * budget / 100
    else:
        print("Invalid season! Please choose between {Summer} and {Winter}.")
else:
    print("Not Enough money to rent a car! Please come back to us when you have enough! Thank you!")

# print
print(class_type)
print(f"{car_type} - {car_price:.2f}")
