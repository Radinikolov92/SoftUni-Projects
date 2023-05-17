# read
budget = int(input())
season = str(input())
fishermen = int(input())

# calculations
offer = 0
boat_price_spring = 3000
boat_price_summer_and_autumn = 4200
boat_price_winter = 2600
discount_for_6_people = 10 / 100
discount_for_7_11_people = 15 / 100
discount_for_12_people = 25 / 100
discount_even_number = 5 / 100

# logic
if season == "Spring":
    if 0 <= fishermen <= 6:
        offer = boat_price_spring - (discount_for_6_people * boat_price_spring)
        if fishermen % 2 == 0:
            offer = offer - (discount_even_number * offer)
        else:
            offer = boat_price_spring - (discount_for_6_people * boat_price_spring)
    elif 7 <= fishermen <= 11:
        offer = boat_price_spring - (discount_for_7_11_people * boat_price_spring)
        if fishermen % 2 == 0:
            offer = offer - (discount_even_number * offer)
        else:
            offer = boat_price_spring - (discount_for_7_11_people * boat_price_spring)
    elif 12 <= fishermen:
        offer = boat_price_spring - (discount_for_12_people * boat_price_spring)
        if fishermen % 2 == 0:
            offer = offer - (discount_even_number * offer)
        else:
            offer = boat_price_spring - (discount_for_12_people * boat_price_spring)
    else:
        print("Invalid number of people! please specify!")
elif season == "Summer" or season == "Autumn":
    if 0 <= fishermen <= 6:
        offer = boat_price_summer_and_autumn - (discount_for_6_people * boat_price_summer_and_autumn)
        if season == "Summer":
            if fishermen % 2 == 0:
                offer = offer - (discount_even_number * offer)
            else:
                offer = boat_price_summer_and_autumn - (discount_for_6_people * boat_price_summer_and_autumn)
        else:
            offer = boat_price_summer_and_autumn - (discount_for_6_people * boat_price_summer_and_autumn)
    elif 7 <= fishermen <= 11:
        offer = boat_price_summer_and_autumn - (discount_for_7_11_people * boat_price_summer_and_autumn)
        if season == "Summer":
            if fishermen % 2 == 0:
                offer = offer - (discount_even_number * offer)
            else:
                offer = boat_price_summer_and_autumn - (discount_for_7_11_people * boat_price_summer_and_autumn)
        else:
            offer = boat_price_summer_and_autumn - (discount_for_7_11_people * boat_price_summer_and_autumn)
    elif 12 <= fishermen:
        offer = boat_price_summer_and_autumn - (discount_for_12_people * boat_price_summer_and_autumn)
        if season == "Summer":
            if fishermen % 2 == 0:
                offer = offer - (discount_even_number * offer)
            else:
                offer = boat_price_summer_and_autumn - (discount_for_12_people * boat_price_summer_and_autumn)
        else:
            offer = boat_price_summer_and_autumn - (discount_for_12_people * boat_price_summer_and_autumn)
    else:
        print("Invalid number of people! please specify!")
elif season == "Winter":
    if 0 <= fishermen <= 6:
        offer = boat_price_winter - (discount_for_6_people * boat_price_winter)
        if fishermen % 2 == 0:
            offer = offer - (discount_even_number * offer)
        else:
            offer = boat_price_winter - (discount_for_6_people * boat_price_winter)
    elif 7 <= fishermen <= 11:
        offer = boat_price_winter - (discount_for_7_11_people * boat_price_winter)
        if fishermen % 2 == 0:
            offer = offer - (discount_even_number * offer)
        else:
            offer = boat_price_winter - (discount_for_7_11_people * boat_price_winter)
    elif 12 <= fishermen:
        offer = boat_price_winter - (discount_for_12_people * boat_price_winter)
        if fishermen % 2 == 0:
            offer = offer - (discount_even_number * offer)
        else:
            offer = boat_price_winter - (discount_for_12_people * boat_price_winter)
    else:
        print("Invalid number of people! please specify!")
else:
    print("Invalid season! Please specify!")

# Print
if offer <= budget:
    excess = budget - offer
    print(f"Yes! You have {excess:.2f} leva left.")
else:
    deficit = offer - budget
    print(f"Not enough money! You need {deficit:.2f} leva.")
