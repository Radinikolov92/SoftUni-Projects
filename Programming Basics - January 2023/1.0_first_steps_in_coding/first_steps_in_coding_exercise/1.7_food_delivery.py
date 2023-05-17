# Read_entry
number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

# Read_prices
price_for_chicken_menu = float(10.35)
price_for_fish_menu = float(12.40)
price_for_vegetarian_menu = float(8.15)
price_for_delivery = float(2.50)
desert_percent = float(20)

# logic
total_for_chicken_menus = float(number_of_chicken_menus * price_for_chicken_menu)
total_for_fish_menus = float(number_of_fish_menus * price_for_fish_menu)
total_for_vegetarian_menus = float(number_of_vegetarian_menus * price_for_vegetarian_menu)

total_without_delivery = float(total_for_chicken_menus + total_for_fish_menus + total_for_vegetarian_menus)

price_for_desert = float((total_without_delivery * desert_percent) / 100)

overall_total = float(total_without_delivery + price_for_desert + price_for_delivery)

# print
print("%.2f" % round(overall_total, 2))
