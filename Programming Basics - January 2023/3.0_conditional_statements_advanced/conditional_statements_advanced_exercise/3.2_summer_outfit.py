# read
temperature = int(input())
time_of_day = str(input())

# logic
Outfit = "N/A"
Shoes = "N/A"
if 10 <= temperature <= 18:
    if time_of_day == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif time_of_day == "Afternoon" or time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    else:
        print("Invalid time of day! Please pick between: {Morning}, {Afternoon} or {Evening}.")
elif 18 < temperature <= 24:
    if time_of_day == "Morning" or time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    else:
        print("Invalid time of day! Please pick between: {Morning}, {Afternoon} or {Evening}.")
elif 25 <= temperature:
    if time_of_day == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif time_of_day == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif time_of_day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    else:
        print("Invalid time of day! Please pick between: {Morning}, {Afternoon} or {Evening}.")
else:
    print("Its too cold outside! Stay home and be safe!")

# print
print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
