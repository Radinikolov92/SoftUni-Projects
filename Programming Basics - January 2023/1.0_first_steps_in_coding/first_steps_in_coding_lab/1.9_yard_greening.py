yard_size = float(input())
price = float(7.61)
price_for_greening = yard_size * price
discount = 0.18 * price_for_greening
offer = price_for_greening - discount
print(f"The final price is: {offer} lv.")
print(f"The discount is: {discount} lv.")