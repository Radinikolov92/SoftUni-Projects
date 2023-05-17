# read prices
puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
miniature_price = 8.20
truck_price = 2

# read
excursion_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
miniatures = int(input())
trucks = int(input())

# logic
puzzles_sum = puzzles * puzzle_price
talking_dolls_sum = talking_dolls * talking_doll_price
teddy_bears_sum = teddy_bears * teddy_bear_price
miniatures_sum = miniatures * miniature_price
trucks_sum = trucks * truck_price

toys_order = puzzles + talking_dolls + teddy_bears + miniatures + trucks
total_sum = puzzles_sum + talking_dolls_sum + teddy_bears_sum + miniatures_sum + trucks_sum

if toys_order >= 50:
    total_sum -= (total_sum * 25 / 100)

total_sum_with_expenses = total_sum - (total_sum * 10 / 100)
excess_amount = total_sum_with_expenses - excursion_price
deficit_amount = excursion_price - total_sum_with_expenses

# print
if total_sum_with_expenses >= excursion_price:
    print(f"Yes! {excess_amount:.2f} lv left. ")
else:
    print(f"Not enough money! {deficit_amount:.2f} lv needed.")
