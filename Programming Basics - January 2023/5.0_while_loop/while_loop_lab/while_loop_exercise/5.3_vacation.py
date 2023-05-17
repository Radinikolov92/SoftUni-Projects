# read
vacation_cost = float(input())
available_money = float(input())

# logic
days_passed = 0
days_spending = 0
exchange = 0
while True:
    if days_spending == 5:
        print("You can't save the money.")
        print(f"{days_passed}")
        break
    else:
        action = str(input())
        money = float(input())

    if action == "spend":
        available_money = available_money - money
        days_spending += 1
        days_passed += 1
        if available_money <= 0:
            available_money = 0
    elif action == "save":
        available_money = available_money + money
        days_spending = 0
        days_passed += 1
        if available_money >= vacation_cost:
            print(f"You saved the money for {days_passed} days.")
            break
        else:
            continue
    else:
        print("Invalid Operation!")
        continue
