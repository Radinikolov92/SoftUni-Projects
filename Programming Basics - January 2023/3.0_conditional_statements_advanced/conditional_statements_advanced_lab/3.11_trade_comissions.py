# read
city = str(input())
sales = float(input())

# logic
commission = 0
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 5 / 100 * sales
        print(f"{commission:.2f}")
    elif 500 < sales <= 1000:
        commission = 7 / 100 * sales
        print(f"{commission:.2f}")
    elif 1000 < sales <= 10000:
        commission = 8 / 100 * sales
        print(f"{commission:.2f}")
    elif 10000 < sales:
        commission = 12 / 100 * sales
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5 / 100 * sales
        print(f"{commission:.2f}")
    elif 500 < sales <= 1000:
        commission = 8 / 100 * sales
        print(f"{commission:.2f}")
    elif 1000 < sales <= 10000:
        commission = 12 / 100 * sales
        print(f"{commission:.2f}")
    elif 10000 < sales:
        commission = 14.5 / 100 * sales
        print(f"{commission:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5 / 100 * sales
        print(f"{commission:.2f}")
    elif 500 < sales <= 1000:
        commission = 7.5 / 100 * sales
        print(f"{commission:.2f}")
    elif 1000 < sales <= 10000:
        commission = 10 / 100 * sales
        print(f"{commission:.2f}")
    elif 10000 < sales:
        commission = 13 / 100 * sales
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")
