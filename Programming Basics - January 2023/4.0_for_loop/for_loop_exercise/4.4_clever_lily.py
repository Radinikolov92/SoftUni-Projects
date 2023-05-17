# read
age = int(input())
price_laundry_machine = float(input())
price_toy = int(input())

# logic
money = 10
money_taken = 1
money_saved = 0
toys_collected = 0
money_from_toys = 0
for i in range(1, age + 1):
    if not(i % 2 == 0):
        toys_collected += 1
        money_from_toys = toys_collected * price_toy
    else:
        money_saved += money - money_taken
        money += 10
total_balance = money_saved + money_from_toys
if total_balance >= price_laundry_machine:
    excess = total_balance - price_laundry_machine
    print(f"Yes! {excess:.2f}")
else:
    deficit = abs(total_balance - price_laundry_machine)
    print(f"No! {deficit:.2f}")
