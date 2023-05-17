# read
defining_number = int(input())

# logic
summ_numbers = 0
while True:
    current_number = int(input())
    summ_numbers += current_number
    if summ_numbers >= defining_number:
        print(summ_numbers)
        break
    else:
        continue
