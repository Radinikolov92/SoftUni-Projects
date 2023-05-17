# read
month = str(input())
hours_spent = int(input())
number_of_people = int(input())
time_of_day = str(input())

# prices
first_3_d = 10.50
first_3_n = 8.40
second_3_d = 12.60
second_3_n = 10.20

# logic
price_per_person = 0
total_price = 0
if time_of_day == "day":
    if month == "march" or month == "april" or month == "may":
        if 4 <= number_of_people:
            first_3_d = first_3_d - (10 * first_3_d / 100)
            total_price = number_of_people * (hours_spent * first_3_d)
            price_per_person = first_3_d
        else:
            total_price = number_of_people * (hours_spent * first_3_d)
            price_per_person = first_3_d
        if 5 <= hours_spent:
            first_3_d = first_3_d - (50 * first_3_d / 100)
            total_price = number_of_people * (hours_spent * first_3_d)
            price_per_person = first_3_d
        else:
            total_price = number_of_people * (hours_spent * first_3_d)
            price_per_person = first_3_d

    elif month == "june" or month == "july" or month == "august":
        if 4 <= number_of_people:
            second_3_d = second_3_d - (10 * second_3_d / 100)
            total_price = number_of_people * (hours_spent * second_3_d)
            price_per_person = second_3_d
        else:
            total_price = number_of_people * (hours_spent * second_3_d)
            price_per_person = second_3_d
        if 5 <= hours_spent:
            second_3_d = second_3_d - (50 * second_3_d / 100)
            total_price = number_of_people * (hours_spent * second_3_d)
            price_per_person = second_3_d
        else:
            total_price = number_of_people * (hours_spent * second_3_d)
            price_per_person = second_3_d
elif time_of_day == "night":
    if month == "march" or month == "april" or month == "may":
        if 4 <= number_of_people:
            first_3_n = first_3_n - (10 * first_3_n / 100)
            total_price = number_of_people * (hours_spent * first_3_n)
            price_per_person = first_3_n
        else:
            total_price = number_of_people * (hours_spent * first_3_n)
            price_per_person = first_3_n
        if 5 <= hours_spent:
            first_3_n = first_3_n - (50 * first_3_n / 100)
            total_price = number_of_people * (hours_spent * first_3_n)
            price_per_person = first_3_n
        else:
            total_price = number_of_people * (hours_spent * first_3_n)
            price_per_person = first_3_n

    elif month == "june" or month == "july" or month == "august":
        if 4 <= number_of_people:
            second_3_n = second_3_n - (10 * second_3_n / 100)
            total_price = number_of_people * (hours_spent * second_3_n)
            price_per_person = second_3_n
        else:
            total_price = number_of_people * (hours_spent * second_3_n)
            price_per_person = second_3_n
        if 5 <= hours_spent:
            second_3_n = second_3_n - (50 * second_3_n / 100)
            total_price = number_of_people * (hours_spent * second_3_n)
            price_per_person = second_3_n
        else:
            total_price = number_of_people * (hours_spent * second_3_n)
            price_per_person = second_3_n
# print
print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
