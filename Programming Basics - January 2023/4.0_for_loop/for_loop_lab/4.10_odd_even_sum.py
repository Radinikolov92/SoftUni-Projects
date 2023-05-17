# read
number_of_cycles = int(input())

# logic
even_sum_numbers = 0
odd_sum_numbers = 0
for value in range(1, number_of_cycles + 1):
    numbers = int(input())
    if value % 2 == 0:
        even_sum_numbers += numbers
    else:
        odd_sum_numbers += numbers

if even_sum_numbers == odd_sum_numbers:
    print(f"Yes")
    print(f"Sum = {even_sum_numbers}")
else:
    difference = abs(even_sum_numbers - odd_sum_numbers)
    print(f"No")
    print(f"Diff = {difference}")
