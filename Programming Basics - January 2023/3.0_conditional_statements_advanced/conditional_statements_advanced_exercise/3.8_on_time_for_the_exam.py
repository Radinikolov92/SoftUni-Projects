# read
hours_of_exam = int(input())
minutes_of_exam = int(input())
hours_of_arrival = int(input())
minutes_of_arrival = int(input())

# logic
time_in_min_exam = hours_of_exam * 60 + minutes_of_exam
time_in_min_arrival = hours_of_arrival * 60 + minutes_of_arrival
difference = time_in_min_exam - time_in_min_arrival

if 30 < difference:
    print("Early")
elif 0 > difference:
    print("Late")
else:
    print("On time")

hh = 0
mm = abs(difference)
result = ""

if mm >= 60:
    hh = mm // 60
    mm = mm % 60

if hh > 0:
    result += f"{hh}:{mm:02d} hours "
elif mm > 0:
    result += f"{mm} minutes "

if difference > 0:
    result += "before the start"
elif difference < 0:
    result += "after the start"

# print
print(result)
