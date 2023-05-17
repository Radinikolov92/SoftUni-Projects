# read
fruit = str(input())
day = str(input())
quantity = float(input())

# read prices
banana = "N/A"
apple = "N/A"
orange = "N/A"
grapefruit = "N/A"
kiwi = "N/A"
pineapple = "N/A"
grapes = "N/A"
total_price = 0

# logic
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    banana = 2.50
    apple = 1.20
    orange = 0.85
    grapefruit = 1.45
    kiwi = 2.70
    pineapple = 5.50
    grapes = 3.85
    if fruit == "banana":
        total_price = quantity * banana
        print(f"{total_price:.2f}")
    elif fruit == "apple":
        total_price = quantity * apple
        print(f"{total_price:.2f}")
    elif fruit == "orange":
        total_price = quantity * orange
        print(f"{total_price:.2f}")
    elif fruit == "grapefruit":
        total_price = quantity * grapefruit
        print(f"{total_price:.2f}")
    elif fruit == "kiwi":
        total_price = quantity * kiwi
        print(f"{total_price:.2f}")
    elif fruit == "pineapple":
        total_price = quantity * pineapple
        print(f"{total_price:.2f}")
    elif fruit == "grapes":
        total_price = quantity * grapes
        print(f"{total_price:.2f}")
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    banana = 2.70
    apple = 1.25
    orange = 0.90
    grapefruit = 1.60
    kiwi = 3.00
    pineapple = 5.60
    grapes = 4.20
    total_price = "N/A"
    if fruit == "banana":
        total_price = quantity * banana
        print(f"{total_price:.2f}")
    elif fruit == "apple":
        total_price = quantity * apple
        print(f"{total_price:.2f}")
    elif fruit == "orange":
        total_price = quantity * orange
        print(f"{total_price:.2f}")
    elif fruit == "grapefruit":
        total_price = quantity * grapefruit
        print(f"{total_price:.2f}")
    elif fruit == "kiwi":
        total_price = quantity * kiwi
        print(f"{total_price:.2f}")
    elif fruit == "pineapple":
        total_price = quantity * pineapple
        print(f"{total_price:.2f}")
    elif fruit == "grapes":
        total_price = quantity * grapes
        print(f"{total_price:.2f}")
    else:
        print("error")
else:
    print("error")
