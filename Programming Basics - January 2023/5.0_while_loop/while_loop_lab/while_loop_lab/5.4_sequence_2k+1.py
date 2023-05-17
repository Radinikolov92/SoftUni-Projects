# read
number = int(input())

# logic
counter = 1
while True:
    if counter <= number:
        print(counter)
        counter = 2 * counter + 1
        continue
    else:
        break
