# read
budget = float(input())
season = str(input())

# variables
destination = "N/A"
residence = "N/A"
expenses = 0

# logic
if 0 <= budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        residence = "Camp"
        expenses = 30 / 100 * budget
        print(f"Somewhere in {destination}")
        print(f"{residence} - {expenses:.2f}")
    elif season == "winter":
        residence = "Hotel"
        expenses = 70 / 100 * budget
        print(f"Somewhere in {destination}")
        print(f"{residence} - {expenses:.2f}")
    else:
        print("Invalid season! Please choose between {Summer} and {Winter}.")
elif 101 <= budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        residence = "Camp"
        expenses = 40 / 100 * budget
        print(f"Somewhere in {destination}")
        print(f"{residence} - {expenses:.2f}")
    elif season == "winter":
        residence = "Hotel"
        expenses = 80 / 100 * budget
        print(f"Somewhere in {destination}")
        print(f"{residence} - {expenses:.2f}")
    else:
        print("Invalid season! Please choose between {Summer} and {Winter}.")
elif 1000 < budget:
    destination = "Europe"
    residence = "Hotel"
    expenses = 90 / 100 * budget
    print(f"Somewhere in {destination}")
    print(f"{residence} - {expenses:.2f}")
else:
    print("Invalid number! Please specify!")
