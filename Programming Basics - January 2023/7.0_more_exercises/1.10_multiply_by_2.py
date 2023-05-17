# logic
allNonNegative = True
while allNonNegative:
    number = float(input())
    if number >= 0:
        result = number * 2
        print(f"Result: {result:.2f}")
    else:
        allNonNegative = False
        print(f"Negative number!")
