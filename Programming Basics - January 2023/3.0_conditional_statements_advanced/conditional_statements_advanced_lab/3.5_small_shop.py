# read
product = str(input())
city = str(input())
quantity = float(input())

# logic

# product prices
coffee = "N/A"
water = "N/A"
beer = "N/A"
sweets = "N/A"
peanuts = "N/A"
total_price = "N/A"

# calculations
if city == "Sofia":
    coffee = 0.50
    water = 0.80
    beer = 1.20
    sweets = 1.45
    peanuts = 1.60
    if product == "coffee":
        total_price = quantity * coffee
    elif product == "water":
        total_price = quantity * water
    elif product == "beer":
        total_price = quantity * beer
    elif product == "sweets":
        total_price = quantity * sweets
    elif product == "peanuts":
        total_price = quantity * peanuts
    else:
        print("We are sorry, we don't have that product in stock!"
              " Please choose between: {coffee}, {water}, {beer}, {sweets} or {peanuts}.")

elif city == "Plovdiv":
    coffee = 0.40
    water = 0.70
    beer = 1.15
    sweets = 1.30
    peanuts = 1.50
    if product == "coffee":
        total_price = quantity * coffee
    elif product == "water":
        total_price = quantity * water
    elif product == "beer":
        total_price = quantity * beer
    elif product == "sweets":
        total_price = quantity * sweets
    elif product == "peanuts":
        total_price = quantity * peanuts
    else:
        print("We are sorry, we don't have that product in stock!"
              " Please choose between: {coffee}, {water}, {beer}, {sweets} or {peanuts}.")

elif city == "Varna":
    coffee = 0.45
    water = 0.70
    beer = 1.10
    sweets = 1.35
    peanuts = 1.55
    if product == "coffee":
        total_price = quantity * coffee
    elif product == "water":
        total_price = quantity * water
    elif product == "beer":
        total_price = quantity * beer
    elif product == "sweets":
        total_price = quantity * sweets
    elif product == "peanuts":
        total_price = quantity * peanuts
    else:
        print("We are sorry, we don't have that product in stock!"
              " Please choose between: {coffee}, {water}, {beer}, {sweets} or {peanuts}.")
else:
    print("We are sorry! We don't have a store in that city! Please choose between: {Sofia}, {Plovdiv} or {Varna}.")

# print
print(f"{total_price}")
