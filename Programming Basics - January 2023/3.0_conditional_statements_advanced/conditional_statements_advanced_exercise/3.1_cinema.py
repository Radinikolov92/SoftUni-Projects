# read
type_of_projection = str(input())
rows = int(input())
columns = int(input())

# logic
income = 0
capacity = rows * columns

# read prices
premiere = 12
normal = 7.50
discount = 5

if type_of_projection == "Premiere":
    income = capacity * premiere
    print(f"{income:.2f} leva")
elif type_of_projection == "Normal":
    income = capacity * normal
    print(f"{income:.2f} leva")
elif type_of_projection == "Discount":
    income = capacity * discount
    print(f"{income:.2f} leva")
else:
    print("Not a valid type! Please choose between: {Premiere}, {Normal} or {Discount}.")
