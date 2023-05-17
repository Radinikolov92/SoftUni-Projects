# read
day_of_the_weak = str(input())

# logic
if day_of_the_weak == "Monday" or day_of_the_weak == "Tuesday" \
        or day_of_the_weak == "Wednesday" or day_of_the_weak == "Thursday" or day_of_the_weak == "Friday":
    print("Working day")
elif day_of_the_weak == "Saturday" or day_of_the_weak == "Sunday":
    print("Weekend")
else:
    print("Error")
