# read
budget = float(input())
season = str(input())
housing = "N/A"
location = "N/A"
price = float(0)

# logic
if 0 <= budget <= 1000:
    housing = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 65 / 100 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 45 / 100 * budget
    else:
        print("Invalid Season! Please pick between {Summer} or {Winter}!")
elif 1000 < budget <= 3000:
    housing = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 80 / 100 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 60 / 100 * budget
    else:
        print("Invalid Season! Please pick between {Summer} or {Winter}!")
elif 3000 < budget:
    housing = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = 90 / 100 * budget
    elif season == "Winter":
        location = "Morocco"
        price = 90 / 100 * budget
    else:
        print("Invalid Season! Please pick between {Summer} or {Winter}!")
else:
    print("Not enough money for vacation! Please contact us when you have enough money. Thank you in advance!")

# print
print(f"{location} - {housing} - {price:.2f}")
