# logic
while True:
    money_saved = 0
    destination = str(input())
    if destination == "End":
        break
    else:
        minimal_budget = float(input())
        while money_saved < minimal_budget:
            money = float(input())
            money_saved += money
            continue
        else:
            print(f"Going to {destination}!")
