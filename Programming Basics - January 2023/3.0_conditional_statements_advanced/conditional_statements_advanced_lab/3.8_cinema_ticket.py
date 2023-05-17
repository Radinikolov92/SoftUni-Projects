# read
day = str(input())

# logic
ticket_price = "N/A"
if day == "Monday" or day == "Tuesday" or day == "Friday":
    ticket_price = 12
elif day == "Wednesday" or day == "Thursday":
    ticket_price = 14
elif day == "Saturday" or day == "Sunday":
    ticket_price = 16
else:
    print("Invalid day of the week!")

# print
print(ticket_price)
