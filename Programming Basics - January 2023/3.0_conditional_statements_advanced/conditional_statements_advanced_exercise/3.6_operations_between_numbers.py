# read
N1 = int(input())
N2 = int(input())
operator = input()

# logic
if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        N_type = "even"
        print(f"{N1} {operator} {N2} = {result} - {N_type}")
    else:
        N_type = "odd"
        print(f"{N1} {operator} {N2} = {result} - {N_type}")
elif operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        N_type = "even"
        print(f"{N1} {operator} {N2} = {result} - {N_type}")
    else:
        N_type = "odd"
        print(f"{N1} {operator} {N2} = {result} - {N_type}")
elif operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        N_type = "even"
        print(f"{N1} {operator} {N2} = {result} - {N_type}")
    else:
        N_type = "odd"
        print(f"{N1} {operator} {N2} = {result} - {N_type}")
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
else:
    print("Unknown operation!")
