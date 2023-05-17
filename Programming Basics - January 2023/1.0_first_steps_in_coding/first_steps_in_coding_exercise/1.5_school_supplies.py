# read
price_of_pens = float(5.80)
price_of_pencils = float(7.20)
price_of_detergent_for_liter = float(1.20)

number_of_pens = int(input())
number_of_pencils = int(input())
detergent_liters = int(input())
discount_percentage = int(input()) / 100

# logic
total_price_for_pens = (float(number_of_pens * price_of_pens))
total_price_for_pencils = (float(number_of_pencils * price_of_pencils))
total_price_for_detergent = (float(detergent_liters * price_of_detergent_for_liter))
total_price_for_materials = (float(total_price_for_pens + total_price_for_pencils + total_price_for_detergent))
discount = (float(total_price_for_materials)) - (float(total_price_for_materials * discount_percentage))

# print
print(float(discount))
