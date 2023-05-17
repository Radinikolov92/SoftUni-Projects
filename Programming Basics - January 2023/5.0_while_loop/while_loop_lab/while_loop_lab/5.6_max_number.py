# logic
import sys
number = input()
Max = -sys.maxsize

while number != "Stop":
    num = int(number)

    if num > Max:
        Max = num
    number = input()

print(Max)
