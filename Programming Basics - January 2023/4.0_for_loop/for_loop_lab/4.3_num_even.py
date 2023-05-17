# read
n = int(input())

# logic
for number in range(n + 1):
    if number % 2 == 0:
        number = 2 ** number
        print(number)
