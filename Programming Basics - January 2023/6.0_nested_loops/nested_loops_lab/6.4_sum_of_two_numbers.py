# read
beginning = int(input())
end = int(input())
magic_number = int(input())

# logic
counter = 0
condition = False
for number1 in range(beginning, end + 1):
    for number2 in range(beginning, end + 1):
        counter += 1
        if number1 + number2 == magic_number:
            condition = True
            print(f"Combination N:{counter} ({number1} + {number2} = {magic_number})")
            break
    if condition:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")
