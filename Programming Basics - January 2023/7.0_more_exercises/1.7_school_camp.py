# read
season = str(input())
group_type = str(input())
number_of_students = int(input())
number_of_nights = int(input())

boys_or_girls_price = 0
mixed_price = 0
total_price = 0
activity = "N/A"
discount = 0
payment = 0

# logic
if season == "Winter":
    if group_type == "boys":
        boys_or_girls_price = 9.60
        total_price = number_of_students * (number_of_nights * boys_or_girls_price)
        activity = "Judo"
    elif group_type == "girls":
        boys_or_girls_price = 9.60
        total_price = number_of_students * (number_of_nights * boys_or_girls_price)
        activity = "Gymnastics"
    elif group_type == "mixed":
        mixed_price = 10
        total_price = number_of_students * (number_of_nights * mixed_price)
        activity = "Ski"
    else:
        print("Invalid group type! Please choose between {boys}, {girls} or {mixed}.")

elif season == "Spring":
    if group_type == "boys":
        boys_or_girls_price = 7.20
        total_price = number_of_students * (number_of_nights * boys_or_girls_price)
        activity = "Tennis"
    elif group_type == "girls":
        boys_or_girls_price = 7.20
        total_price = number_of_students * (number_of_nights * boys_or_girls_price)
        activity = "Athletics"
    elif group_type == "mixed":
        mixed_price = 9.50
        total_price = number_of_students * (number_of_nights * mixed_price)
        activity = "Cycling"
    else:
        print("Invalid group type! Please choose between {boys}, {girls} or {mixed}.")
elif season == "Summer":
    if group_type == "boys":
        boys_or_girls_price = 15
        total_price = number_of_students * (number_of_nights * boys_or_girls_price)
        activity = "Football"
    elif group_type == "girls":
        boys_or_girls_price = 15
        total_price = number_of_students * (number_of_nights * boys_or_girls_price)
        activity = "Volleyball"
    elif group_type == "mixed":
        mixed_price = 20
        total_price = number_of_students * (number_of_nights * mixed_price)
        activity = "Swimming"
    else:
        print("Invalid group type! Please choose between {boys}, {girls} or {mixed}.")
else:
    print("Invalid season! Please pick between {Winter} , {Spring} or {Summer}.")
if 50 <= number_of_students:
    discount = 50 / 100 * total_price
    payment = total_price - discount
elif 20 <= number_of_students < 50:
    discount = 15 / 100 * total_price
    payment = total_price - discount
elif 10 <= number_of_students < 20:
    discount = 5 / 100 * total_price
    payment = total_price - discount
else:
    payment = total_price

# print
print(f"{activity} {payment:.2f} lv.")
