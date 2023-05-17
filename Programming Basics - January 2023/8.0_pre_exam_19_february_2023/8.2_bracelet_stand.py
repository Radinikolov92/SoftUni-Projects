# read
pocket_money = float(input())
earnings = float(input())
expenses = float(input())
gift_price = float(input())

# logic
days = 5
saved_pocket_money = days * pocket_money
saved_earned_money = days * earnings
total_saved_money = saved_pocket_money + saved_earned_money
final_income = total_saved_money - expenses

if final_income >= gift_price:
    print(f"Profit: {final_income:.2f} BGN, the gift has been purchased.")
else:
    deficit = abs(final_income - gift_price)
    print(f"Insufficient money: {deficit:.2f} BGN.")
