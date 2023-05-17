# read
month = str(input())
duration = int(input())

# variables
studio_price = 0
apartment_price = 0
studio_total = 0
apartment_total = 0

# logic
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    discount_7_may_oct = 5 / 100 * studio_price
    discount_14_may_oct = 30 / 100 * studio_price
    discount_14_apart = 10 / 100 * apartment_price
    studio_total = duration * studio_price
    apartment_total = duration * apartment_price
    if 7 < duration <= 14:
        studio_price = studio_price - discount_7_may_oct
        studio_total = duration * studio_price
        apartment_total = duration * apartment_price
        print(f"Apartment: {apartment_total:.2f} lv.")
        print(f"Studio: {studio_total:.2f} lv.")
    elif 14 < duration:
        studio_price = studio_price - discount_14_may_oct
        apartment_price = apartment_price - discount_14_apart
        studio_total = duration * studio_price
        apartment_total = duration * apartment_price
        print(f"Apartment: {apartment_total:.2f} lv.")
        print(f"Studio: {studio_total:.2f} lv.")
    else:
        print(f"Apartment: {apartment_total:.2f} lv.")
        print(f"Studio: {studio_total:.2f} lv.")
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    discount_14_june_sep = 20 / 100 * studio_price
    discount_14_apart = 10 / 100 * apartment_price
    studio_total = duration * studio_price
    apartment_total = duration * apartment_price
    if 14 < duration:
        studio_price = studio_price - discount_14_june_sep
        apartment_price = apartment_price - discount_14_apart
        studio_total = duration * studio_price
        apartment_total = duration * apartment_price
        print(f"Apartment: {apartment_total:.2f} lv.")
        print(f"Studio: {studio_total:.2f} lv.")
    else:
        print(f"Apartment: {apartment_total:.2f} lv.")
        print(f"Studio: {studio_total:.2f} lv.")
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    discount_14_apart = 10 / 100 * apartment_price
    studio_total = duration * studio_price
    apartment_total = duration * apartment_price
    if 14 < duration:
        apartment_price = apartment_price - discount_14_apart
        studio_total = duration * studio_price
        apartment_total = duration * apartment_price
        print(f"Apartment: {apartment_total:.2f} lv.")
        print(f"Studio: {studio_total:.2f} lv.")
    else:
        print(f"Apartment: {apartment_total:.2f} lv.")
        print(f"Studio: {studio_total:.2f} lv.")
else:
    print("We do not provide services during this month.")
