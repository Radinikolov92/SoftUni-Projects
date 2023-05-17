# read
food_for_puppy_kg = int(input())

# logic
food_for_puppy_g = food_for_puppy_kg * 1000
food_given = 0
command = input()
while True:
    if command == "Adopted":
        if food_given <= food_for_puppy_g:
            excess = food_for_puppy_g - food_given
            print(f"Food is enough! Leftovers: {excess} grams.")
        else:
            deficit = abs(food_for_puppy_g - food_given)
            print(f"Food is not enough. You need {deficit} grams more.")
        break
    else:
        food_given += int(command)
        command = input()
        continue
