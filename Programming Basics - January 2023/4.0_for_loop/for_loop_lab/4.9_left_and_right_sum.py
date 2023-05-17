# read
number = int(input())

# logic
left_sum = 0

for value in range(1, number + 1):
    left_sum = left_sum + int(input())
right_sum = 0
for value in range(1, number + 1):
    right_sum = right_sum + int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(right_sum - left_sum)
    print(f"No, diff = {difference}")
