# read
fuel_type = str(input())
fuel_liters = float(input())

# logic
if fuel_type == "Diesel":
    Diesel = "diesel"
    if fuel_liters >= 25:
        print(f"You have enough {Diesel}.")
    else:
        print(f"Fill your tank with {Diesel}!")
elif fuel_type == "Gasoline":
    Gasoline = "gasoline"
    if fuel_liters >= 25:
        print(f"You have enough {Gasoline}.")
    else:
        print(f"Fill your tank with {Gasoline}!")
elif fuel_type == "Gas":
    Gas = "gas"
    if fuel_liters >= 25:
        print(f"You have enough {Gas}.")
    else:
        print(f"Fill your tank with {Gas}!")
else:
    print("Invalid fuel!")
