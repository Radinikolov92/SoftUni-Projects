# read
import sys
max_number = -sys.maxsize
summ_of_numbers = 0
number_of_cycles = int(input())

# logic
for value in range(0, number_of_cycles):
    number = int(input())
    if number > max_number:
        max_number = number
    summ_of_numbers += number

if max_number == summ_of_numbers - max_number:
    print("Yes")
    print(f"Sum = {summ_of_numbers - max_number}")
else:
    print("No")
    summ_of_numbers = summ_of_numbers - max_number
    print(f"Diff = {abs(max_number - summ_of_numbers)}")
