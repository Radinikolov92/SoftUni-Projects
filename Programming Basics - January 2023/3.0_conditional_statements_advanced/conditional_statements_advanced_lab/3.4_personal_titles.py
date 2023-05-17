# read
age = float(input())
gender = str(input())

# logic
if gender == "m":
    if 16 <= age:
        print("Mr.")
    else:
        print("Master")
elif gender == "f":
    if 16 <= age:
        print("Ms.")
    else:
        print("Miss")
else:
    print("Invalid Gender!")
