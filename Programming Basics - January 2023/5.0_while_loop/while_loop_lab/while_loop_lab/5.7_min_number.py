# logic
import sys
number = input()
Min = sys.maxsize

while number != "Stop":
    num = int(number)

    if num < Min:
        Min = num
    number = input()

print(Min)
