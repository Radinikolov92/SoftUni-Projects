# read
days = int(input())
accommodation = str(input())
experience = str(input())

# prices
room_for_one_person = 18
apartment = 25
president_apartment = 35

# logic
nights = days - 1
total = 0
total_with_discount = 0
final = 0
if accommodation == "room for one person":
    total = nights * room_for_one_person
    if experience == "positive":
        final = total + (25 / 100 * total)
    elif experience == "negative":
        final = total - (10 / 100 * total)
    else:
        print("Please share your experience with us! {positive} or {negative}.")
elif accommodation == "apartment":
    total = nights * apartment
    if 0 < days <= 10:
        total_with_discount = total - (30 / 100 * total)
    elif 10 < days <= 15:
        total_with_discount = total - (35 / 100 * total)
    elif 15 < days:
        total_with_discount = total - (50 / 100 * total)
    else:
        print("Invalid number of days!")
    if experience == "positive":
        final = total_with_discount + (25 / 100 * total_with_discount)
    elif experience == "negative":
        final = total_with_discount - (10 / 100 * total_with_discount)
    else:
        print("Please share your experience with us! {positive} or {negative}.")
elif accommodation == "president apartment":
    total = nights * president_apartment
    if 0 < days <= 10:
        total_with_discount = total - (10 / 100 * total)
    elif 10 < days <= 15:
        total_with_discount = total - (15 / 100 * total)
    elif 15 < days:
        total_with_discount = total - (20 / 100 * total)
    else:
        print("Invalid number of days!")
    if experience == "positive":
        final = total_with_discount + (25 / 100 * total_with_discount)
    elif experience == "negative":
        final = total_with_discount - (10 / 100 * total_with_discount)
    else:
        print("Please share your experience with us! {positive} or {negative}.")

else:
    print("Unknown accommodation! Please pick between: {room for one person}, {apartment} or {president apartment}.")

# print
print(f"{final:.2f}")
