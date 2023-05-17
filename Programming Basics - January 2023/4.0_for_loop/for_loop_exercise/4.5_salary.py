# read
import math

number_of_tabs = int(input())
salary = int(input())

# logic
fine = 0
balance = 0
for check in range(1, number_of_tabs + 1):
    name_of_website = str(input())
    if name_of_website == "Facebook":
        fine += 150
        balance = salary - fine
        if balance <= 0:
            print("You have lost your salary.")
            break
        else:
            continue
    else:
        balance = salary - fine
    if name_of_website == "Instagram":
        fine += 100
        balance = salary - fine
        if balance <= 0:
            print("You have lost your salary.")
            break
        else:
            continue
    else:
        balance = salary - fine
    if name_of_website == "Reddit":
        fine += 50
        balance = salary - fine
        if balance <= 0:
            print("You have lost your salary.")
            break
        else:
            continue
    else:
        balance = salary - fine
else:
    print(math.floor(balance))
