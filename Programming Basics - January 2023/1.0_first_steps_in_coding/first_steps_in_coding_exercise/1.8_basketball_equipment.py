# console_read
year_tax = int(input())

# prices
shoes_percent = int(40)
shirt_and_trousers_percent = int(20)
basketball = int(4)
accessories = int(5)

# logic
price_shoes = float(year_tax - (year_tax * shoes_percent / 100))
price_shirt_and_trousers = float(price_shoes - (price_shoes * shirt_and_trousers_percent / 100))
price_basketball = float(price_shirt_and_trousers / basketball)
price_of_accessories = float(price_basketball / accessories)
total = float(year_tax + price_shoes + price_shirt_and_trousers + price_basketball + price_of_accessories)

# print
print("%.2f" % round(total, 2))
