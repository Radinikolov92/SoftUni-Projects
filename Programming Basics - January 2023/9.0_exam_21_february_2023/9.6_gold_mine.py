# read
number_of_locations = int(input())
for locations in range(1, number_of_locations + 1):
    gold_average = 0
    gold_vault = 0
    expected_gold_output = float(input())
    days_excavating = int(input())
    for days in range(1, days_excavating + 1):
        gold_excavated = float(input())
        gold_vault += gold_excavated
    else:
        gold_average = gold_vault / days_excavating
        if gold_average >= expected_gold_output:
            print(f"Good job! Average gold per day: {gold_average:.2f}.")
        else:
            deficit = expected_gold_output - gold_average
            print(f"You need {deficit:.2f} gold.")
