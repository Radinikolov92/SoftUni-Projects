# read prices
VIP_ticket = 499.99
Normal_ticket = 249.99
percent_1_to_4 = 75
percent_5_to_9 = 60
percent_10_to_24 = 50
percent_25_to_49 = 40
percent_50_above = 25
transport_price = 0
tickets_price = 0
net_budget = 0
expenses = 0
deficit = 0

# read
budget = float(input())
category = str(input())
number_of_people = int(input())

# logic
if 1 <= number_of_people <= 4:
    transport_price = 75 * budget / 100
    net_budget = budget - transport_price
    if category == "VIP":
        tickets_price = number_of_people * VIP_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    elif category == "Normal":
        tickets_price = number_of_people * Normal_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")

elif 5 <= number_of_people <= 9:
    transport_price = 60 * budget / 100
    net_budget = budget - transport_price
    if category == "VIP":
        tickets_price = number_of_people * VIP_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    elif category == "Normal":
        tickets_price = number_of_people * Normal_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    else:
        print("Invalid Category!")

elif 10 <= number_of_people <= 24:
    transport_price = 50 * budget / 100
    net_budget = budget - transport_price
    if category == "VIP":
        tickets_price = number_of_people * VIP_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    elif category == "Normal":
        tickets_price = number_of_people * Normal_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    else:
        print("Invalid Category!")

elif 25 <= number_of_people <= 49:
    transport_price = 40 * budget / 100
    net_budget = budget - transport_price
    if category == "VIP":
        tickets_price = number_of_people * VIP_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    elif category == "Normal":
        tickets_price = number_of_people * Normal_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    else:
        print("Invalid Category!")

elif 50 <= number_of_people:
    transport_price = 25 * budget / 100
    net_budget = budget - transport_price
    if category == "VIP":
        tickets_price = number_of_people * VIP_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    elif category == "Normal":
        tickets_price = number_of_people * Normal_ticket
        expenses = net_budget - tickets_price
        if 0 <= expenses:
            print(f"Yes! You have {expenses:.2f} leva left.")
        else:
            deficit = tickets_price - net_budget
            print(f"Not enough money! You need {deficit:.2f} leva.")
    else:
        print("Invalid Category!")
else:
    print("Invalid Number of People!")
